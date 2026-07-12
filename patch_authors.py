import sys

with open('src/data.ts', 'r') as f:
    content = f.read()

content = content.replace(
    'authors: "Betsy Muriithi-Ochieng\', Alvin Igobwa, George Okello"',
    'authors: "Betsy Muriithi, Alvin Mugwe, George O. Ouma"'
)

content = content.replace(
    'authors: "Dr. Hema Latha Krishna (APU), George Okello Ouma (The ResourceEdge)"',
    'authors: "George O. Ouma"'
)

content = content.replace(
    'authors: "George Okello Ouma (The ResourceEdge)"',
    'authors: "George O. Ouma"'
)

with open('src/data.ts', 'w') as f:
    f.write(content)

