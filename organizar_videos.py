#!/usr/bin/env python3
"""
Organizador Centralizado de Videos Compilados de Precálculo 2
============================================================
Copia y sincroniza todos los videos finales renderizados desde `media/videos/`
hacia una estructura unificada y limpia organizada por capítulos:

    videos_compilados/
    ├── capitulo_05/
    │   ├── Ejercicio05_02.mp4
    │   ├── ...
    │   └── Ejercicio05_78.mp4
    └── capitulo_06/
        ├── Ejercicio06_02.mp4
        └── ...

Si existen múltiples versiones (ej. 480p15 y 4K 2160p60), selecciona automáticamente
la versión de mayor resolución disponible.
"""

import os
import re
import shutil
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
MEDIA_DIR = ROOT_DIR / "media" / "videos"
EXPORT_DIR = ROOT_DIR / "videos"

# Jerarquía de resolución (mayor puntaje = mayor prioridad)
QUALITY_RANK = {
    "2160p60": 50,  # 4K Ultra HD
    "1440p60": 40,  # 2K QHD
    "1080p60": 30,  # Full HD
    "720p30": 20,   # HD estándar
    "480p15": 10,   # Calidad rápida
}

def sync_compiled_videos() -> dict:
    pattern_ch = re.compile(r"Ejercicio(\d+)_(\d+)\.mp4$", re.IGNORECASE)
    pattern_jh = re.compile(r"EjercicioJh_?(\d+)\.mp4$", re.IGNORECASE)
    best_videos = {}

    if not MEDIA_DIR.exists():
        print(f"⚠️  No se encontró la carpeta de medios: {MEDIA_DIR}")
        return {}

    # Escanear recursivamente todos los videos renderizados
    for mp4_path in MEDIA_DIR.rglob("*.mp4"):
        # Ignorar fragmentos parciales de Manim
        if "partial_movie_files" in mp4_path.parts:
            continue

        match_ch = pattern_ch.search(mp4_path.name)
        match_jh = pattern_jh.search(mp4_path.name)

        if match_ch:
            cap_num = int(match_ch.group(1))
            ej_num = int(match_ch.group(2))
            key = (cap_num, ej_num)
            dest_dir_name = f"capitulo_{cap_num:02d}"
        elif match_jh:
            ej_num = int(match_jh.group(1))
            key = ("jh", ej_num)
            dest_dir_name = "jhoselyn"
        else:
            continue

        # Determinar resolución a partir de la carpeta padre
        res_folder = mp4_path.parent.name
        score = QUALITY_RANK.get(res_folder, 0)
        mtime = mp4_path.stat().st_mtime

        # Priorizar versiones más recientes (código actualizado) o a tiempo similar mayor calidad
        if (key not in best_videos or 
            mtime > best_videos[key]["mtime"] + 30 or 
            (abs(mtime - best_videos[key]["mtime"]) <= 30 and score > best_videos[key]["score"])):
            best_videos[key] = {
                "dest_dir": dest_dir_name,
                "src_path": mp4_path,
                "resolution": res_folder,
                "score": score,
                "mtime": mtime,
                "filename": mp4_path.name,
                "size_mb": mp4_path.stat().st_size / (1024 * 1024),
            }

    # Copiar/actualizar en videos_compilados/
    results_by_cap = {}
    EXPORT_DIR.mkdir(parents=True, exist_ok=True)

    for key, data in sorted(best_videos.items(), key=lambda item: str(item[0])):
        dest_folder = EXPORT_DIR / data["dest_dir"]
        dest_folder.mkdir(parents=True, exist_ok=True)

        dest_file = dest_folder / data["filename"]

        # Copiar solo si no existe o si el origen es más reciente / diferente tamaño
        needs_copy = True
        if dest_file.exists():
            if dest_file.stat().st_size == data["src_path"].stat().st_size:
                needs_copy = False

        if needs_copy:
            shutil.copy2(data["src_path"], dest_file)

        results_by_cap.setdefault(data["dest_dir"], []).append({
            **data,
            "dest_path": dest_file,
            "copied": needs_copy,
        })

    return results_by_cap

def main():
    print("\n" + "=" * 70)
    print("📁 Sincronizando Videos Compilados en 'videos_compilados/'")
    print("=" * 70)

    results = sync_compiled_videos()
    if not results:
        print("❌ No se encontraron videos finales para sincronizar.")
        return 1

    total_videos = 0
    total_size = 0.0

    for group_name, items in sorted(results.items()):
        header_name = f"Capítulo {group_name.replace('capitulo_', '')}" if group_name.startswith("capitulo_") else group_name.capitalize()
        print(f"\n📂 {header_name} ({len(items)} videos):")
        print("-" * 70)
        for item in sorted(items, key=lambda x: str(x.get("ej", ""))):
            total_videos += 1
            total_size += item["size_mb"]
            status = "🔄 Actualizado" if item["copied"] else "✔️  Al día"
            res_tag = f"[{item['resolution']}]"
            print(f"  • {item['filename']:<20} {res_tag:<11} {item['size_mb']:>5.2f} MB  {status}")

    print("\n" + "=" * 70)
    print(f"✨ Sincronización exitosa: {total_videos} videos organizados ({total_size:.2f} MB total).")
    print(f"📍 Ubicación: {EXPORT_DIR.resolve()}")
    print("=" * 70 + "\n")
    return 0

if __name__ == "__main__":
    main()
