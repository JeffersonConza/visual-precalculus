#!/usr/bin/env python3
"""
CLI de Automatización de Renders para Visual Precalculus
=========================================================
Facilita la compilación de ejercicios en Manim y la generación automática de vistas
previas GIF optimizadas en distintas resoluciones (480p hasta 4K).

Uso:
    python render.py 5.2                   # Render rápido en 480p15 + GIF
    python render.py 5.4 --high            # Render en 1080p60 (Full HD)
    python render.py 5.2 --4k              # Render en 4K Ultra HD
    python render.py --list                # Listar ejercicios disponibles
    python render.py all --low             # Renderizar todos los ejercicios en 480p
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

# Directorio raíz del proyecto
ROOT_DIR = Path(__file__).resolve().parent

# Configuración de perfiles de calidad de Manim
QUALITY_PROFILES = {
    "low": {"flag": "-ql", "res": "480p15", "desc": "480p @ 15fps (Desarrollo rápido)"},
    "med": {"flag": "-qm", "res": "720p30", "desc": "720p @ 30fps (HD estándar)"},
    "high": {"flag": "-qh", "res": "1080p60", "desc": "1080p @ 60fps (Full HD - Producción)"},
    "prod": {"flag": "-qp", "res": "1440p60", "desc": "1440p @ 60fps (2K QHD)"},
    "4k": {"flag": "-qk", "res": "2160p60", "desc": "3840x2160 @ 60fps (4K Ultra HD)"},
}

def discover_exercises() -> dict[str, dict]:
    """
    Escanea el repositorio en busca de archivos de ejercicios (ej_XX_YY.py)
    y detecta automáticamente la clase de escena que hereda de AmarunExerciseScene o Scene.
    Omite directorios virtuales (.venv, .git) para compatibilidad multiplataforma (Windows/Linux/WSL).
    """
    exercises = {}
    pattern = re.compile(r"ej_(\d+)_(\d+)\.py$")
    class_pattern = re.compile(r"class\s+(Ejercicio\w+)\s*\(")

    # Recorrido seguro omitiendo carpetas del sistema, entornos virtuales y binarios
    for root, dirs, files in os.walk(ROOT_DIR, onerror=lambda err: None):
        dirs[:] = [
            d for d in dirs
            if not d.startswith(".")
            and d not in ("media", "docs", "images", "otros", "__pycache__", "build", "dist")
        ]
        for file_name in files:
            match = pattern.search(file_name)
            if match:
                py_file = Path(root) / file_name
                cap_num = int(match.group(1))
                ej_num = int(match.group(2))
                key = f"{cap_num}.{ej_num}"
                padded_key = f"{cap_num:02d}_{ej_num:02d}"

                try:
                    content = py_file.read_text(encoding="utf-8")
                    class_match = class_pattern.search(content)
                    class_name = class_match.group(1) if class_match else f"Ejercicio{padded_key}"
                except Exception:
                    class_name = f"Ejercicio{padded_key}"

                exercises[key] = {
                    "key": key,
                    "file_path": py_file,
                    "rel_path": py_file.relative_to(ROOT_DIR),
                    "class_name": class_name,
                    "stem": f"ej_{padded_key}",
                    "chapter": cap_num,
                    "exercise": ej_num,
                }
                # Alias alternativos (ej: 05_02 o ej_05_02)
                exercises[padded_key] = exercises[key]
                exercises[f"ej_{padded_key}"] = exercises[key]

    return exercises

def normalize_key(input_str: str) -> str:
    """Normaliza variantes como '5.2', '05.02', '05_02' a formato '5.2'."""
    clean = input_str.strip().lower().replace("ej_", "")
    parts = re.split(r"[._]", clean)
    if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
        return f"{int(parts[0])}.{int(parts[1])}"
    return input_str

def render_exercise(
    info: dict,
    quality: str = "low",
    generate_gif: bool = True,
    preview: bool = False,
    extra_flags: list = None
) -> bool:
    """Ejecuta la renderización con Manim y opcionalmente genera el GIF con ffmpeg."""
    profile = QUALITY_PROFILES[quality]
    file_rel = info["rel_path"].as_posix()
    class_name = info["class_name"]

    print("\n" + "=" * 65)
    print(f"🎬 Renderizando Ejercicio {info['key']}: {class_name}")
    print(f"📁 Archivo: {file_rel}")
    print(f"⚙️  Calidad: {profile['desc']}")
    print("=" * 65)

    manim_bin = shutil.which("manim") or "manim"
    cmd = [manim_bin, profile["flag"], file_rel, class_name]
    if preview:
        cmd.append("-p")
    if extra_flags:
        cmd.extend(extra_flags)

    print(f"▶️  Ejecutando: {' '.join(cmd)}")
    use_shell = sys.platform == "win32"
    result = subprocess.run(cmd, cwd=ROOT_DIR, shell=use_shell)

    if result.returncode != 0:
        print(f"❌ Error al renderizar {class_name} con Manim.")
        return False

    # Localizar video de salida
    media_dir = ROOT_DIR / "media" / "videos" / info["stem"] / profile["res"]
    video_path = media_dir / f"{class_name}.mp4"

    if not video_path.exists():
        # Búsqueda alternativa por nombre
        candidates = list((ROOT_DIR / "media").rglob(f"{class_name}.mp4"))
        if candidates:
            video_path = candidates[0]

    print(f"✅ Video generado: {video_path}")

    # Generación opcional de GIF para previsualización
    if generate_gif and video_path.exists():
        gif_dir = ROOT_DIR / "docs" / "previews"
        gif_dir.mkdir(parents=True, exist_ok=True)
        gif_path = gif_dir / f"{info['stem']}.gif"

        print(f"🖼️  Generando GIF de previsualización en: {gif_path.relative_to(ROOT_DIR)}")
        ffmpeg_bin = shutil.which("ffmpeg") or "ffmpeg"
        ffmpeg_cmd = [
            ffmpeg_bin, "-y", "-i", str(video_path),
            "-vf", "fps=10,scale=480:-1:flags=lanczos",
            str(gif_path)
        ]
        gif_res = subprocess.run(ffmpeg_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=use_shell)
        if gif_res.returncode == 0:
            print(f"🎉 GIF guardado exitosamente: {gif_path}")
        else:
            print("⚠️  No se pudo generar el GIF con FFmpeg.")

    return True

def main():
    parser = argparse.ArgumentParser(
        description="CLI de Automatización de Renders para Visual Precalculus (Editorial Amarun / Yachay Tech)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  python render.py 5.2                  Render rápido (480p15) + GIF de vista previa
  python render.py 5.4 --high           Render Full HD (1080p60) para YouTube o clase
  python render.py 5.2 --4k             Render de máxima resolución (4K UHD)
  python render.py --list               Muestra los ejercicios disponibles
  python render.py all --high           Renderiza todos los ejercicios en 1080p
        """
    )

    parser.add_argument(
        "exercise",
        nargs="?",
        default=None,
        help="Número del ejercicio (ej. 5.2, 5.4) o 'all' para todos."
    )

    # Banderas de calidad
    q_group = parser.add_mutually_exclusive_group()
    q_group.add_argument("-l", "--low", action="store_const", const="low", dest="quality", help="Calidad baja (480p 15fps) - Por defecto")
    q_group.add_argument("-m", "--med", action="store_const", const="med", dest="quality", help="Calidad media (720p 30fps)")
    q_group.add_argument("-H", "--high", action="store_const", const="high", dest="quality", help="Calidad alta (1080p 60fps - Full HD)")
    q_group.add_argument("-p", "--prod", action="store_const", const="prod", dest="quality", help="Calidad producción (1440p 60fps - 2K)")
    q_group.add_argument("-k", "--4k", action="store_const", const="4k", dest="quality", help="Calidad máxima (2160p 60fps - 4K UHD)")

    parser.add_argument("--no-gif", action="store_true", help="No generar vista previa GIF automática")
    parser.add_argument("-P", "--preview", action="store_true", help="Abrir reproductor de video automáticamente al terminar")
    parser.add_argument("--list", action="store_true", help="Listar ejercicios disponibles y salir")

    args, unknown = parser.parse_known_args()

    # Calidad por defecto
    quality = args.quality or "low"
    generate_gif = not args.no_gif

    # Descubrir ejercicios
    exercises = discover_exercises()
    # Filtrar claves canónicas (evitar duplicados de alias)
    canonical = {k: v for k, v in exercises.items() if "." in k}

    if args.list or not args.exercise:
        print("\n📚 Ejercicios Detectados en el Repositorio:")
        print("-" * 55)
        for key in sorted(canonical.keys(), key=lambda x: [int(p) for p in x.split(".")]):
            info = canonical[key]
            gif_exists = (ROOT_DIR / "docs" / "previews" / f"{info['stem']}.gif").exists()
            status = "✅ GIF Listo" if gif_exists else "⏳ Pendiente"
            print(f"  • Ejercicio {key:>4} : {info['class_name']:<18} ({status}) -> {info['rel_path']}")
        print("-" * 55)
        print("💡 Para renderizar: python render.py <num_ejercicio> [--high | --4k]")
        return 0

    target = args.exercise.strip().lower()

    if target == "all":
        print(f"🚀 Renderizando TODOS los ejercicios ({len(canonical)}) en calidad {quality.upper()}...")
        success_count = 0
        for key in sorted(canonical.keys(), key=lambda x: [int(p) for p in x.split(".")]):
            ok = render_exercise(canonical[key], quality=quality, generate_gif=generate_gif, preview=args.preview, extra_flags=unknown)
            if ok:
                success_count += 1
        print(f"\n✨ Proceso completado: {success_count}/{len(canonical)} ejercicios renderizados con éxito.")
        return 0 if success_count == len(canonical) else 1

    # Buscar ejercicio específico
    norm_key = normalize_key(target)
    if norm_key in exercises:
        ok = render_exercise(exercises[norm_key], quality=quality, generate_gif=generate_gif, preview=args.preview, extra_flags=unknown)
        return 0 if ok else 1
    else:
        print(f"❌ Ejercicio '{args.exercise}' no encontrado.")
        print(f"Ejercicios disponibles: {', '.join(sorted(canonical.keys()))}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
