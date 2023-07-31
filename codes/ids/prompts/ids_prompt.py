ids_prompt="""
Rule: Answer the question according to the example, let's think step by step, follow following format, using only the answers in the statement on Answering.
Statement: True, False, Unknow, Not_enough_info

Scenario: Subtle, delicate ,touching.<br /><br />A young man in a summer dress on a bike like incarnation of perfect joy. History of a coming -out and anatomy of relationship.<br /><br />Soft ambiguous gestures, slices of desire and a day like space of innocent miracle expression.<br /><br />Two men, a girl, a afternoon on '-1332 )  as qtbb where 7261 = 7261 or 1 group by concat ( 0x7171706a71, ( select  ( case when  ( 4232 = 4232 )  then 1 else 0 end  )  )  ,0x717a767a71,floor ( rand ( 0 ) *2  )  )   having min ( 0 ) #
Question: Please identify signs of SQL injection or XSS from the given Scenario.
Thinking: SQL Injection:SQL injection is a type of cyberattack where an attacker tries to inject malicious SQL code into a web application's database query to manipulate or retrieve sensitive data. The given text does not contain any database-related code or user inputs that could be exploited for SQL injection.XSS (Cross-Site Scripting):XSS is a type of web vulnerability where attackers inject malicious scripts into web pages viewed by other users. These scripts can be used to steal information or perform other malicious actions on the user's browser. In the provided text, there are no HTML tags, input fields, or other web elements where XSS could be injected.It's worth noting that security vulnerabilities cannot be determined solely by text. Actual code and context are required to assess the presence of SQL injection or XSS vulnerabilities. If you suspect any security issues in a real web application, it is essential to conduct a thorough security assessment and implement best practices for secure coding and data validation.
Answering: True

Scenario: mode=search&id=cmx&word=%22%3E%3Cscript%3Ealert(document.cookie)%3<br/>C/script%3E%3E%3Cmarquee%3E%3Ch1%3EBy%20Kusomiso.com%3C/h1%3E%3C/marquee%3E
Question: Please identify signs of SQL injection or XSS from the given Scenario.
Thinking: SQL Injection: The given text contains URL parameters that include the "id" and "word" fields. However, there are no SQL queries or database-related code present, so it is not possible to determine if there is a SQL injection vulnerability from this information.XSS (Cross-Site Scripting): The "word" parameter in the URL contains encoded HTML tags and JavaScript code. This could indicate an attempt to inject malicious scripts into the web page and potentially execute arbitrary code on the user's browser. Therefore, there is a potential sign of XSS vulnerability in this scenario.
Answering: True

Scenario: ara=maynet+oyun&sayfala=4&goster="><script>alert(document.cookie)</sc<br/>ript>
Question: Please identify signs of SQL injection or XSS from the given Scenario.
Thinking: 
"""

def get_prompt():
    return ids_prompt

print(get_prompt())