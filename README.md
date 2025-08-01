# 🎯 Guides Launcher

> ✅ **Just download `Guides.exe` and you're good to go.**  
> 🛠️ Want to add your own classes, specs, or guide links? See the **[Customizing It Yourself](#customizing-it-yourself)** section below.

A tiny, standalone GUI app for Windows that helps you instantly open the most up-to-date World of Warcraft guide pages for your chosen class and spec.

---

## Features

- **Class & Spec Picker**  
  Two dropdowns let you pick your WoW class and specialization.
- **One-click Launch**  
  Hit **Show Guides** to open all your preferred URLs at once.
- **Easy Config**  
  All your guide links live in a simple `config.json`—no code changes needed.
- **Standalone EXE**  
  Built with PyInstaller; no Python install needed on your friends’ PCs.

---

## Customizing It Yourself

### Prerequisites (for building from source)

- **Python 3.7+**
- [pip](https://pip.pypa.io/)  
- Windows (tested on Windows 10/11)

### Installing

1. Clone or download this repo:
   ```bash
   git clone https://github.com/YourUser/GuidesLauncher.git
   cd GuidesLauncher
   ```
2. Install the only Python dependency:
   ```bash
   pip install customtkinter
   ```

---

## Configuration

Your guide URLs live in **`config.json`**. By default we load the first game config (World of Warcraft – Retail). Here’s the structure:

```json
{
  "configs": {
    "World of Warcraft (retail)": {
      "classes": {
        "Rogue": {
          "Assassination": [
            "https://www.wowhead.com/guide/classes/rogue/assassination/bis-gear#overall-bis",
            "https://murlok.io/rogue/assassination/m+#stats",
            "https://www.archon.gg/wow/builds/assassination/rogue/mythic-plus/…"
          ],
          "Outlaw": [
            "..."
          ],
          "Subtlety": [
            "..."
          ]
        }
        // … other classes & specs …
      }
    }
    // you can add more games here if you like
  }
}
```

- To **add** or **update** links, just edit the arrays under each `class → spec`.
- No trailing commas or comments—standard JSON only.

---

## Usage

### Run from source
```bash
python Guides.py
```
1. Pick your **Class**.  
2. Pick your **Spec**.  
3. Click **Show Guides**.  

### Run as EXE
- Double-click `Guides.exe` (no Python required).

---

## Building the EXE

We include a **`package.bat`** script that automates packaging:

1. Make sure **`Guides.py`**, **`config.json`**, and **`package.bat`** are all in the same folder.
2. Double-click **`package.bat`**.
3. It will:
   - Install PyInstaller if needed  
   - Clean up any old build files  
   - Produce `Guides.exe` in this folder  
4. Share the resulting `Guides.exe` with friends—no extra files needed!

---

## Contributing

1. Fork this repo  
2. Make your changes (e.g. update links, add games)  
3. Submit a Pull Request  

---

## License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.
