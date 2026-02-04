# How to Update Amazon Links

## Option 1: Edit the JSON file yourself

1. Open `books.json`
2. Replace `YOUR_ASIN_HERE` with the actual Amazon ASIN (looks like `B0ABCD1234`)
3. Save the file
4. Tell Skippy "update the Amazon links from books.json"

That's it! Skippy will update all the HTML files automatically.

## Option 2: Just send Skippy the ASINs

Send a message like:
```
Remember When 1950s: B0ABCD1234
Sunday Drive: B0EFGH5678
Main Street: B0IJKL9012
```

Skippy will update books.json and rebuild the pages.

---

## Amazon ASIN Format
ASINs look like: `B0ABCD1234` (10 characters, starts with B0)

You can find them in the KDP dashboard or in the Amazon URL:
`amazon.com/dp/B0ABCD1234` ← that's the ASIN
