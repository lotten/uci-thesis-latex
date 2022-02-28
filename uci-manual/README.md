# UCI Thesis Manual

This directory contains the UCI thesis manual used to develop this latex template. As the manual changes, the template must be updated to match.

The scripts in this directory make it easy to download the most recent manual from UCI's web site and identify any differences from the version implemented by this template.

# Dependencies

- Python 3: tested with version 3.10.2
- Python packages:
  - beautifulsoup4: tested with version 4.9.3
  - requests: tested with version 2.27.1
  - urllib3: tested with version 1.26.7
  
# How to get the updated manual

Just run the script:

```
./scrape_manual.py
```
This will download and parse the most recent version of the manual from UCI's website.

# Check if there was any update

After downloading a fresh copy of the manual, you should check if there is any difference between the newly downloaded manual and the last one stored in this repository. You can do that running the following command:

```
git diff manual/*.md
```

## Report updates

Depending on the result of the `diff` command, you may follow one of the following steps:

1. **There are no differences:** then the template should be correct, and you are good to go :)

2. **There are trivial differences:** If there are small differences that **do not affect** the actual requirements, then please do one of these two things:
  - Either [create an issue](https://github.com/lotten/uci-thesis-latex/issues) in GitHub using the title "Trivial Update".
  - Or even better, update and commit only the new `.md` files by yourself and submit a pull request.

3. **If there are relevant differences:** If there are differences that **affect** the requirements, maybe the the template needs to be updated. To help keeping it up-to-date please do one of these two things:
   - [Create an issue](https://github.com/lotten/uci-thesis-latex/issues) in GitHub using an appropriate title like "New requirement XYZ". Please add details describing the changes that need to be made to the template.
   - Or, if you'd like to update the template yourself, 
     - Edit/Update the latex template.
     - Update the `.md` files.
     - Commit the changes.
     - Submit a pull request on GitHub.
