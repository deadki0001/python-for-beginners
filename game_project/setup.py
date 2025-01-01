from cx_Freeze import setup, Executable
import os

# List of additional files to include (e.g., images, sounds)
additional_files = [("namek.png", "namek.png"),
                    ("kiblast.mp3", "kiblast.mp3"),
                    ("goku2.png", "goku2.png"),
                    ("entrance_video1.mp4", "entrance_video1.mp4"),
                    # Add more files here as needed
                   ]

setup(
    name="Dragonball Z - Mini-Hero's",
    version="1.0",
    description="A Dragonball Z themed 2D fighting game",
    options={"build_exe": {"include_files": additional_files}},
    executables=[
        Executable("game_dev.py", target_name="dragonball_game.exe", icon="game_icon.ico")
    ]
)
