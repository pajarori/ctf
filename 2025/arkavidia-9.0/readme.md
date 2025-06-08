---
title: Arkavidia 9.0 Quals
date: 2025-03-15
team: N2L - Sotong Always Sad
member:
  - pajarori
  - 53buahapel
  - kirisaki
---

# [miscellaneous] 

## 100% free flag {#100%freeflag}
### overview
  Pada chall ini, terdapat flag namun terbalik textnya, tinggal reverse untuk mendapatkan flag yang benar.

### flag
  ARKAV{GoodLuck_and_HaveFun_SampaiJumpaDiBandung}

## beat frendy {#beatfrendy}
### overview
  Pada chall ini kita harus mengalahkan ai catur yang di deploy di server, untuk ini kami menggunakan ai juga buat nge beat nya disini kami pake [stockfish](https://stockfishchess.org/) kami buat skill level ke mentok di 20 biar jago.

### code
  [beatfrendy.py](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2025/arkavidia-9.0/files/beatfrendy.py)

### flag
  ARKAV{hanya_sepuh_yang_berani_make_opening_g2-g4}

## babyeth {#babyeth}
### overview
  Goal pada chall ini adalah buat nge drain balance, kalo kita lihat dari script BabyETH.sol:
  ```solidity showLineNumbers
  // SPDX-License-Identifier: MIT
  pragma solidity ^0.8.0;

  contract BabyETH {
      mapping(address => uint256) public balances;

      function deposit() public payable {
          balances[msg.sender] += msg.value;
      }

      function withdraw(uint256 amount) public {
          uint256 currBalance = balances[msg.sender];
          require(currBalance >= amount, "Insufficient balance");

          (bool success, ) = msg.sender.call{value: amount}("");
          require(success, "Transfer failed");
          
          currBalance -= amount;
          balances[msg.sender] = currBalance;
      }

      // Function to receive ETH
      receive() external payable {}
  }
  ```
  Ada bug yaitu dia nge send eth dulu baru ngurangin balance jadi kalau kita panggil withdraw lagi sebelum balance dikurangi itu bisa ngedrain balance BabyETH nya. Untuk itu kita buat script exploitnya dibawah.

### code
  [ExploitBabyeth.sol](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2025/arkavidia-9.0/files/ExploitBabyeth.sol)

### flag
  ARKAV{b4by_dUlu_y4k!!f1n4L_4rKaV_b4rU_so4L_bLokc3nG_h4rD}

## abstract art {#abstractart}
### overview
  Diberikan dua buah gambar badut 🤡🤡. 
  ![abstractart-1](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2025/arkavidia-9.0/files/abstractart-1.png)
  Dua gambar ini gaada bedanya cuma beda scale dan kami tau ini adalah gambar enkripsi yang digenerate namanya piet, buat decodenya kita bisa make [Piet IDE](https://gabriellesc.github.io/piet/) tapi disini kita harus stop in di akhir garis merah itu kalo ga bakal ke loop dan ke replace semua.
  ![abstractart-2](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2025/arkavidia-9.0/files/abstractart-2.png)
  ![abstractart-3](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2025/arkavidia-9.0/files/abstractart-3.png)

### flag
  ARKAV{p1x315_po3try}

# [reverse engineering]

## pyrev {#pyrev}
### overview
  Diberikan python program yang menuliskan machine code langsung ke memori dan menjalankannya untuk memeriksa input (flag). Program tersebut memanipulasi setiap byte dari flag yang kita masukkan, lalu membandingkannya dengan nilai heks tertentu. Cara nge solve nya kita tinggal "membalik" proses itu serta *brute force* byte demi byte—sampai kita menemukan input (flag) yang menghasilkan output hex yang sesuai dengan expected hex. Dengan cara itu, kita bisa mendapatkan flag asli yang valid.

### code
  [pyrev.py](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2025/arkavidia-9.0/files/pyrev.py)

### flag
  ARKAV{its_just_python_riiiiggghhhhhhtttttt????????}