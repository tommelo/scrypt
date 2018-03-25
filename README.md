# scrypt
Simple Crypt

## About
**Simple Crypt**(scrypt) is a small cli tool that encrypts/decrypts text content using some classic cipher algorithms such as Caesar, Viginere and Vernam Cipher.

## Installation
**scrypt** requires no third-party dependencies. You can get the lastest version by clonning this repository:
```shell
git clone https://github.com/tommelo/scrypt
```

## Usage
```shell
python scrypt.py <options> plaintext
```
The scrypt cli takes one positional argument(plaintext) that represents a text string:
```shell
python scrypt.py -c caesar -e --rot 10 "clear text"
```

See the options overview:

Short opt | Long opt | Default | Required | Description
--------- | -------- | ------- | -------- | -----------
-c        | --cipher      | None    | Yes | the cipher(caesar, viginere or vernam)
-d        | --decrypt     | None    | No  | decrypts the given content
-e        | --encrypt     | None    | No  | encrypts the given content
-h        | --help        | None    | No  | shows the help usage
-i        | --input       | None    | No  | the text file to encrypt/decrypt
-k        | --key         | None    | No  | the encryption key
-o        | --output      | None    | No  | the output file
N/A       | --rot         | 13      | No  | the Caesar cipher offset to rotate
N/A       | --brute-force | False   | No  | Caesar cipher brute force mode
N/A       | --version     | None    | No  | shows the application's current version

## Caesar Cipher

Using the default ROT13 Caesar Cipher algorithm:
```shell
python scrypt.py -c caesar -e "The quick brown fox jumps over the lazy dog"

Gur dhvpx oebja sbk whzcf bire gur ynml qbt
```

```shell
python scrypt.py -c caesar -d "Gur dhvpx oebja sbk whzcf bire gur ynml qbt"

The quick brown fox jumps over the lazy dog
```
Changing the offset rotation:
```shell
python scrypt.py -c caesar --rot 5 -e "The quick brown fox jumps over the lazy dog"

Ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl
```

```shell
python scrypt.py -c caesar --rot 5 -d "Ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"

The quick brown fox jumps over the lazy dog
```

Using the Caesar Cipher brute force mode:
```shell
python scrypt.py -c caesar --brute-force "Ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"

Xli uymgo fvsar jsb nyqtw sziv xli pedc hsk
Wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj
Vjg swkem dtqyp hqz lworu qxgt vjg ncba fqi
Uif rvjdl cspxo gpy kvnqt pwfs uif mbaz eph
The quick brown fox jumps over the lazy dog
Sgd pthbj aqnvm enw itlor nudq sgd kzyx cnf
Rfc osgai zpmul dmv hsknq mtcp rfc jyxw bme
Qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald
Pda mqeyg xnksj bkt fqilo kran pda hwvu zkc
Ocz lpdxf wmjri ajs ephkn jqzm ocz gvut yjb
Nby kocwe vliqh zir dogjm ipyl nby futs xia
Max jnbvd ukhpg yhq cnfil hoxk max etsr whz
Lzw imauc tjgof xgp bmehk gnwj lzw dsrq vgy
Kyv hlztb sifne wfo aldgj fmvi kyv crqp ufx
Jxu gkysa rhemd ven zkcfi eluh jxu bqpo tew
Iwt fjxrz qgdlc udm yjbeh dktg iwt apon sdv
Hvs eiwqy pfckb tcl xiadg cjsf hvs zonm rcu
Gur dhvpx oebja sbk whzcf bire gur ynml qbt
Ftq cguow ndaiz raj vgybe ahqd ftq xmlk pas
Esp bftnv mczhy qzi ufxad zgpc esp wlkj ozr
Dro aesmu lbygx pyh tewzc yfob dro vkji nyq
Cqn zdrlt kaxfw oxg sdvyb xena cqn ujih mxp
Bpm ycqks jzwev nwf rcuxa wdmz bpm tihg lwo
Aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn
Znk waoiq hxuct lud pasvy ubkx znk rgfe jum
```

Using files as input/output:
```shell
python scrypt.py -c caesar -e -i input_file.txt -o encrypted_file.txt
```

```shell
python scrypt.py -c caesar -d -i encrypted_file.txt
```

## Vernam Cipher

Encrypting text with the Vernam Cipher Algorithm:
```shell
python scrypt.py -c vernam --key '$uperS3cretKey' -e -o encrypted_text.txt "The quick brown fox jumps over the lazy dog" 
```

```shell
python scrypt.py -c vernam --key '$uperS3cretKey' -d -i encrypted_text.txt
```

## Viginère Cipher

Encrypting text with the Viginère Cipher Algorithm:
```shell
python scrypt.py -c viginere --key '$uperS3cretKey' -e "The quick brown fox jumps over the lazy dog"

X^VedI|G^eW>UqruWUkS}Y`VhKUpihpZ[93PT`nKJik
```

```shell
python scrypt.py -c viginere --key '$uperS3cretKey' -d 'X^VedI|G^eW>UqruWUkS}Y`VhKUpihpZ[93PT`nKJik'

The quick brown fox jumps over the lazy dog
```

## Piped Input

You can pipe any content to be encrypted/decrypted
```shell
echo 'X^VedI|G^eW>UqruWUkS}Y`VhKUpihpZ[93PT`nKJik' | python scrypt.py -c viginere -d --key '$uperS3cretKey'
```

## Piped Output

The output can also be piped:
```shell
python scrypt.py -c viginere -d --key '$uperS3cretKey' 'X^VedI|G^eW>UqruWUkS}Y`VhKUpihpZ[93PT`nKJik' > decoded_file.txt
```

## License
This is an open-source software licensed under the [MIT license](https://opensource.org/licenses/MIT).
