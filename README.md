# Frostfire Theme

A dual-variant VSCode color theme balancing icy frost blues with vivid fire oranges and reds.

## Variants

| Variant | Background | Accent |
|---|---|---|
| **Frostfire Dark** | `#1A1E2E` deep night blue | `#FF6B35` fire orange + `#88C0D0` ice blue |
| **Frostfire Light** | `#F0F4F8` snow white | `#D94F00` ember red + `#4C87B9` frost blue |

## Color Palette

### Dark

| Role | Color |
|---|---|
| Background | `#1A1E2E` |
| Foreground | `#D8DEE9` |
| Keywords | `#FF6B35` fire orange |
| Functions | `#88C0D0` ice blue |
| Strings | `#A3BE8C` frost green |
| Types / Classes | `#FFD166` ember gold |
| Numbers / Booleans | `#B48EAD` amethyst |
| Comments | `#616E88` muted |
| Errors | `#FF4D6D` hot red |

### Light

| Role | Color |
|---|---|
| Background | `#F0F4F8` |
| Foreground | `#2E3440` |
| Keywords | `#D94F00` ember orange |
| Functions | `#2F6699` steel blue |
| Strings | `#4A7C59` forest green |
| Types / Classes | `#9A6B00` dark gold |
| Numbers / Booleans | `#6E4D8F` deep violet |
| Comments | `#7A8FA8` muted |
| Errors | `#C0392B` crimson |

## Installation

### From source

```bash
git clone https://github.com/eskopp/vscode
cd vscode
# Press F5 in VSCode to launch the Extension Development Host
```

### Via VSIX

```bash
npm install -g @vscode/vsce
vsce package
code --install-extension frostfire-theme-*.vsix
```

## License

MIT
