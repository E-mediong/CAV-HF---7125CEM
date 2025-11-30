"""
Master Script to Generate All Figures for 7125CEM Assignment
Run this script to create all required diagrams and visualizations
"""

import subprocess
import sys
import os

# Ensure proper encoding for Windows console
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print("=" * 70)
print("7125CEM ASSIGNMENT - FIGURE GENERATION")
print("Generating all required figures for submission")
print("=" * 70)
print()

# List of scripts to run
scripts = [
    ('generate_control_structure.py', 'Control Structure Diagram'),
    ('generate_uca_summary.py', 'UCA Summary Analysis'),
    ('generate_part2_diagrams.py', 'Part 2 Human Error Diagrams')
]

# Check if required libraries are installed
print("Checking required libraries...")
required_libs = ['matplotlib', 'numpy']

missing_libs = []
for lib in required_libs:
    try:
        __import__(lib)
        print(f"  [OK] {lib} found")
    except ImportError:
        missing_libs.append(lib)
        print(f"  [MISSING] {lib} NOT found")

if missing_libs:
    print()
    print("ERROR: Missing required libraries!")
    print("Please install them using:")
    print(f"  pip install {' '.join(missing_libs)}")
    sys.exit(1)

print()
print("All required libraries installed!")
print()

# Run each script
total_scripts = len(scripts)
completed = 0

for script_file, description in scripts:
    print(f"[{completed + 1}/{total_scripts}] Generating: {description}")
    print(f"             Running: {script_file}")

    try:
        result = subprocess.run(
            [sys.executable, script_file],
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode == 0:
            print(f"  [SUCCESS] {description}")
            if result.stdout:
                for line in result.stdout.split('\n'):
                    if line.strip():
                        print(f"    {line}")
            completed += 1
        else:
            print(f"  [FAILED] {description}")
            if result.stderr:
                print(f"    Error: {result.stderr}")

    except subprocess.TimeoutExpired:
        print(f"  [TIMEOUT] {description}")
    except Exception as e:
        print(f"  [ERROR] {str(e)}")

    print()

# Summary
print("=" * 70)
print(f"GENERATION COMPLETE: {completed}/{total_scripts} successful")
print("=" * 70)
print()

if completed == total_scripts:
    print("[SUCCESS] All figures generated successfully!")
    print()
    print("Generated Files:")
    print("  PART 1 (STPA Analysis):")
    print("    - Control_Structure_Diagram.png / .pdf")
    print("    - UCA_Summary_Analysis.png / .pdf")
    print()
    print("  PART 2 (Human Error Analysis):")
    print("    - Part2_Endsley_SA_Model.png / .pdf")
    print("    - Part2_Swiss_Cheese_Model.png / .pdf")
    print("    - Part2_Cognitive_Biases_Cascade.png / .pdf")
    print()
    print("You can now insert these figures into your final assignment document.")
    print()
    print("Recommended placement:")
    print("  - Control_Structure_Diagram: After 'Hierarchical Control Structure' section")
    print("  - UCA_Summary_Analysis: After 'STPA Step 1: Unsafe Control Actions' section")
    print("  - Part2_Endsley_SA_Model: In Part 2 'En Route Detection Failure' section")
    print("  - Part2_Swiss_Cheese_Model: In Part 2 conclusion or recommendations")
    print("  - Part2_Cognitive_Biases_Cascade: In Part 2 'Initial Error' section")
else:
    print(f"[WARNING] Only {completed}/{total_scripts} scripts completed successfully")
    print("Please check the errors above and try again.")

print()
print("=" * 70)
