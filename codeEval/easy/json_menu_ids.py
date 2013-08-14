import sys, json
  
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  if test.strip() != "":
    print sum([item['id']
              for item in json.loads(test)['menu']['items'] if item and 'label' in item])
test_cases.close()