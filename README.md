# FR_UNI - Penetration Testing Tool

Welcome to FR_UNI! This README will guide you through the process of setting up and using FR_UNI on macOS, Linux (all major distributions), and Windows.

# Table of Contents

```System Requirements```

```Installation Instructions```

```Usage```

```Uninstallation```

```Troubleshooting```

# System Requirements

**To use FR_UNI, ensure your system meets the following requirements:**

`Processor: 64-bit CPU`

`Memory: Minimum 2GB RAM`

`Disk Space: Minimum 100MB available`

`Python: Version 3.8 or higher`

Dependencies: Listed in `requirements.txt`

# Installation Instructions

## macOS

**Install Homebrew:**

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

**Install Python (if not already installed):**

`brew install python`

**Clone the Repository:**

`git clone https://github.com/your-repository/FR_UNI.git`
`cd FR_UNI`

**Install Dependencies:**

`pip3 install -r requirements.txt`

**Run FR_UNI:**

`python3 fr_uni.py`

## Linux

## Debian/Ubuntu-Based Distributions

**Update Packages:**

`sudo apt update && sudo apt upgrade`

**Install Python:**

`sudo apt install python3 python3-pip git -y`

**Clone the Repository:**

`git clone https://github.com/your-repository/FR_UNI.git`
`cd FR_UNI`

**Install Dependencies:**

`pip3 install -r requirements.txt`

**Run FR_UNI:**

`python3 fr_uni.py`

```Fedora/CentOS/RHEL-Based Distributions```

**Update Packages:**

`sudo dnf update`

**Install Python:**

`sudo dnf install python3 python3-pip git -y`

**Clone the Repository:**

`git clone https://github.com/your-repository/FR_UNI.git`
`cd FR_UNI`

**Install Dependencies:**

`pip3 install -r requirements.txt`

**Run FR_UNI:**

`python3 fr_uni.py`

## Arch-Based Distributions

**Update Packages:**

`sudo pacman -Syu`

**Install Python:**

`sudo pacman -S python python-pip git`

**Clone the Repository:**

`git clone https://github.com/your-repository/FR_UNI.git`
`cd FR_UNI`

**Install Dependencies:**

`pip3 install -r requirements.txt`

**Run FR_UNI:**

`python3 fr_uni.py`

```Windows```

**Install Python:**

`Download Python from python.org.`

*Ensure to select "Add Python to PATH" during installation.*

**Install Git:**

`Download Git from git-scm.com and install it.`

**Clone the Repository:**

*Open Command Prompt or PowerShell and run:*

`git clone https://github.com/your-repository/FR_UNI.git`
`cd FR_UNI`

**Install Dependencies:**

`pip install -r requirements.txt`

**Run FR_UNI:**

`python fr_uni.py`

# Usage

**Navigate to the FR_UNI directory:**

`cd /path/to/FR_UNI`

**Execute the main script:**

`python3 fr_uni.py`

**Follow the on-screen prompts to perform penetration testing tasks. Always ensure you have proper authorization before proceeding.**

# Uninstallation

## To remove FR_UNI:

**Delete the cloned repository:**

`rm -rf /path/to/FR_UNI`

**Optionally, uninstall dependencies:**

`pip3 uninstall -r requirements.txt`

# Troubleshooting

`Permission Denied: Ensure you have appropriate permissions for installation and execution.`

`Missing Python: Verify Python is installed and added to PATH.`

```Dependency Issues: Reinstall dependencies using:```

`pip3 install --force-reinstall -r requirements.txt`

`Contact Support: For further assistance, reach out to [fr.root85@gmail.com].`

