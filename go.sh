
pandoc --from markdown --to docx --mathjax  --no-highlight --reference-doc sw.docx  -o report.docx report.md



# pandoc report.md \
#     -o document.pdf \
#     --template eisvogel.tex \
#     --listings

# pandoc --from markdown+raw_tex --to pptx --no-highlight  -o output.pptx presentation.md


pandoc --from markdown --to docx --no-highlight  --reference-doc ref.docx  -o paper.docx pp.md

# pandoc  paper.md -o test.pdf

