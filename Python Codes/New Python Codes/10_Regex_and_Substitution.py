import re
agentNamesRegex = re.compile(r'Agent (\w)\w*')
print(agentNamesRegex.search('Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.').group(0,1))
agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')