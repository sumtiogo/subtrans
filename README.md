subtrans
=========

偵測檔案編碼，轉成utf-8，然後簡體轉繁體。


Install
-------
    pip install git+https://github.com/sumtiogo/subtrans.git --allow-external jianfan --allow-unverified jianfan

you may need to restart bash

Usage
------

轉換單擋

subtrans file > output


轉換整個資料夾裡的檔案

subtrans dir

會把所有檔案轉換後輸出到加上`.subtrans.srt`的新檔案
