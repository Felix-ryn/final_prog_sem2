# 🚗 Aplikasi Pendataan Kendaraan – Python

A simple **vehicle data recording system** built with **Python**, providing input validation, vehicle age checking, and log storage. Designed for learning **OOP (Object-Oriented Programming)** with encapsulation and inheritance.

---

## 📦 Features

- **Data Input**:
  - Owner name, brand, year, type, license plate, and color
  - Validation using regex for all inputs

- **Validation Rules**:
  - Owner name: letters and spaces only
  - Brand: minimum 2 characters, letters and spaces only
  - Year: between 1980–2025
  - Type: must be `Mobil`, `Motor`, or `Truk`
  - License Plate: format like `AB1234CD`
  - Color: letters and spaces only

- **Vehicle Age Check**:
  - Marks vehicles older than 10 years as "old"
  - Notes newer vehicles as "new"

- **Data Storage**:
  - All valid vehicle data saved in `kendaraan.log`

---

## 🧱 Tech Stack

| Layer      | Technology     |
|------------|----------------|
| Language   | Python 3.x     |
| Libraries  | `re`, `datetime` |
| Storage    | Plain text log (`kendaraan.log`) |

---

## 📁 Project Structure

```yaml
final_prog_sem2/
├── Source code.py          # Main program file
└── kendaraan.log    # Vehicle data log file (created after first run)
```
## 🚀 Getting Started
1. Clone the Repository
```bash
git clone https://github.com/Felix-ryn/final_prog_sem2.git
cd final_prog_sem2
```
2. Run the Program
```bash
python Source code.py
```
3. Follow the Instructions
Input owner name, vehicle brand, year, type, license plate, and color.
Program will validate inputs, display details, check if the vehicle is old, and save data.

## 📖 Example Output
```yaml
Input Kendaraan
Nama pemilik  : Felix Ryan
Merk kendaraan: Toyota
Tahun kendaraan: 2010
Jenis kendaraan (Mobil/Motor/Truk): Mobil
Nomor Polisi (cth: AB1234CD) tanpa spasi: AB1234CD
Warna kendaraan: Hitam

Data oke.
Pemilik     : Felix Ryan
Merk        : Toyota
Tahun       : 2010
Jenis       : Mobil
No Polisi   : AB1234CD
Warna       : Hitam
Catatan: Kendaraan ini termasuk kendaraan tua (lebih dari 10 tahun).
Data disimpan.
```

## 📜 License
MIT License
Copyright (c) 2025 Felix Ryan Agusta

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

## 👨‍💻 Author
Felix Ryan Agusta
GitHub:  [Felix-ryn](https://github.com/Felix-ryn)

“Learning OOP by building simple and functional Python projects.” 🚗
