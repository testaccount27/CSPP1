import os, subprocess, re
'''
"python eval.py Solution.py"
"Result: (.*)/(.*) testcases passed."
'''
def runProcess(command, expr=None):
	run_proc = subprocess.Popen(command, stdout=subprocess.PIPE)
	proc_out = run_proc.stdout.read().decode('utf-8')
	print(proc_out)
	if expr:
		proc_out = re.findall(expr, proc_out)
		tests_passed = int(float(proc_out[0][0]))
		tests_total = int(float(proc_out[0][1]))
		return (tests_passed, tests_total)

cases, totalcases = runProcess("python eval.py Solution.py", "Result: (.*)/(.*) testcases passed.")
score, totalscore = runProcess("pylint Solution.py","Your code has been rated at (.*)/(.*) \(.*\)")

f = open('myfile', 'w')
f.write("number of testcases passed: " + str(cases) + "/" + str(totalcases) + "\npylint score: " + str(score) + "/" + str(totalscore))  # python will convert \n to os.linesep
f.close() 
path = os.getcwd().split('\\')
folder = path[-1]

runProcess("git status")
runProcess("git add .")
runProcess("git commit -m \""+ folder +" -> number of testcases passed: " + str(cases) + "/" + str(totalcases) + " and pylint score: " + str(score) + "/" + str(totalscore) + " \"")
if cases == totalcases:
	runProcess("git push -u origin master")