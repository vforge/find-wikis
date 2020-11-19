# Lazy hack

**Fandom Hackathon Dec 2020** project: Lazy, mass WikiID finder.

## Usage

```bash
$> ./find-wikis.sh
```

Will read list of Fandom wiki URLs from `in.txt` (each URL in new line) and output CSV-compatible data to `out.txt`.txt`

### Or

```bash
$> echo "http://www.fandom.com" | python ./find-wikis.sh
```

Will output in `stdout`.
