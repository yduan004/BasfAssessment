# Run script
This tool can be used to  parse any webpage to find words that are Anagrames or Palindrome in the page.

Run the tool in terminal under the `BasfAssessment` repository: 

```sh
sh script.sh https://raw.githubusercontent.com/yduan004/BasfAssessment/main/test/text.txt
```

Note: users can pass any webpage url, here uses a test url as an example. 

# Run unittest
The python find anagram and palindrome utilities can be tested under the `test` folder by running in terminal:
```sh
cd test
python -m unittest discover
```