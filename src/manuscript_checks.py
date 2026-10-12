"""Data-free checks for the canonical submission manuscript."""
import re


def citation_issues(text):
    if '## References' not in text:
        return ['Missing reference list.']
    body, bibliography = text.split('## References', 1)
    bibliography = bibliography.split('## Main displays')[0]
    entries = re.findall(r'^(\d+)\. (.+)$', bibliography, re.M)
    numbers = [int(number) for number, _ in entries]
    issues = []
    if numbers != list(range(1, len(entries)+1)):
        issues.append('Reference list is not numbered consecutively.')
    seen = []
    for group in re.findall(r'\[(\d+(?:,\d+)*)\]', body):
        for item in group.split(','):
            number = int(item)
            if number not in numbers:
                issues.append(f'Citation {number} has no reference entry.')
            if number not in seen:
                seen.append(number)
    if seen != list(range(1, len(seen)+1)):
        issues.append('Citations are not numbered by first appearance.')
    unused = sorted(set(numbers)-set(seen))
    if unused:
        issues.append(f'Uncited references: {unused}.')
    return issues


def markdown_tables(text):
    tables, current = [], []
    for line in text.splitlines()+['']:
        if line.strip().startswith('|') and line.strip().endswith('|'):
            current.append([cell.strip().replace('**','') for cell in line.strip().strip('|').split('|')])
        elif current:
            table = [current[0]] + [row for row in current[1:]
                     if not all(set(cell) <= set('-: ') for cell in row)]
            if any(len(row) != len(table[0]) for row in table):
                raise ValueError('Markdown table has inconsistent column counts.')
            tables.append(table)
            current = []
    return tables
