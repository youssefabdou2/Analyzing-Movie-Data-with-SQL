# Analyzing Movie Data with SQL

## Quick start
1. Put `mubi_movies_ratings.db` in the same folder.
2. Install required packages:
```bash
pip install pandas matplotlib seaborn wordcloud
```
3. Run the script:
```bash
python "Analyzing Movie Data with SQL.py"
```

## Summary
- Gets a sample movie row.
- Lists recent popular movies (2018+).
- Plots counts of high-rated movies (rating > 4.5) per year (1950+).
- Shows top 10 directors by popularity.
- Creates a word cloud from the most liked critiques.

## Tips
- Use a virtual environment.
- Wrap the SQLite connection in a context manager.
- Remove redundant `hue` from the director popularity plot.
