---
title: Slashroot 8 Quals
date: 2024-10-1
team: N2L - Sigma
member:
  - pajarori
---

# [reverse]

## last {#last}
### overview
Diberikan file binary yang melakukan XOR pada sebuah array string dengan sebuah key string. Untuk merecoverynya tinggal copy paste aja operasinya dan dapatlah string flagnya.
![last-1](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8-final/images/last-1.png)
![last-2](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8-final/images/last-2.png)
### code
[last.py](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8-final/files/last.py)
### flag
slashroot8{hikss_l45t_ch4ll_r3v3r53_3n91n33r1n9_900dbye_CTF}

# [web]

## a-chan {#achan}
### overview
Terdapat vulnerability code injection pada file sendMessage.php, disini tinggal masukan payload untuk rce dan read flag.
![achan-1](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8-final/images/achan-1.png)
![achan-2](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8-final/images/achan-2.png)
![achan-3](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8-final/images/achan-3.png)
### flag
slashroot8{1wni_fwul4wg_dy4rw1_angeluuuu-neeeNYan}

## nodejs enthusiast {#nodejsenthusiast}
### overview
Goals untuk challange ini adalah bypass parameter pada update role sehingga bisa menjadi role admin dan kemudian melakukan SSTI pada parameter name di page admin.
Kita tidak bisa langsung merubah ke role dengan nama admin, Untuk melakukan bypass pada parameter role kita bisa menggunakan Unicode Homoglyphs Attack atau bisa menggunakan [Tools Ini](https://www.irongeek.com/homoglyph-attack-generator.php), disini saya menggunakan string "Àdmin" untuk parameter role.
![nodejsenthusiast-1](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8-final/images/nodejsenthusiast-1.png)
![nodejsenthusiast-2](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8-final/images/nodejsenthusiast-2.png)
![nodejsenthusiast-3](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8-final/images/nodejsenthusiast-3.png)
Untuk ssti beberapa karakter di blacklist dengan regex "/[()]|`|fs|process|require/i". Untuk mengakali ini atau untuk bisa memanggil fungsi tanpa menggunakan tanda kurung dan backtick saya menggunakan instanceof atau dengan [referensi ini](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof) karena:
*"If constructor has a Symbol.hasInstance method, the method will be called in priority, with object as its only argument and constructor as this."* ~ mozilla
![nodejsenthusiast-4](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8-final/images/nodejsenthusiast-4.png)
Pada "obj instanceof constructor" jika constructor adalah "Symbol.hasInstance" obj akan digunakan sebagai parameter dari constructor dan akan dipanggil, untuk ini saya menggunakan eval dan obj isinya payload yang nantinya untuk RCE. Karena ada juga string yang di blacklist saya akan pakai hex payloadnya.
![nodejsenthusiast-5](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8-final/images/nodejsenthusiast-5.png)
### code
[nodejsenthusiast.txt](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8-final/files/nodejsenthusiast.txt)
### flag
slashroot8{now_you_know_how_to_exec_command_without_backticks_and_parentheses}

# [joy]
## gravity dash {#gravitydash}
### overview
Diberikan sebuah executable game yang di build dengan unity goals nya adalah membeli flag dengan 9999 coin dan coin sudah 999999 jadi hanya perlu membeli saja. Disini jika kita game over game akan melakukan save state ke registry dan jika diulang maka game akan otomatis game over terus untuk bisa mengulang hanya perlu merubah value registry. registry ada di "HKEY_CURRENT_USER\Software\DefaultCompany\Gravity Rush\"
![gravitydash-1](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8-final/images/gravitydash-1.png)
![gravitydash-2](https://raw.githubusercontent.com/pajarori/ctf/refs/heads/main/2024/slashroot8-final/images/gravitydash-2.png)
### flag
slashroot8{Th4NkY0u_s0_muCHhhH_4LL_siGn0uT}



