Actually, just like doing sth what TPC have made for PTCG Regional League.
Providing features of show pairing, upload match result, show final pairing, etc...

For backend, mySQL / use XAMPP is needed. 

If need to test, run service on NAS (or sth like local env). 
If really in use, put it on AWS / cloud service.

Cookie is needed to recognize login user. 
Random URL may be used to direct to match_result_report_page. 

Step 1, design static FrontEnd Template. (Completed)
Step 1.5, write .js file
Step 2, setting Backend Env. 
Step 3, use JavaScript to link Front End and BackEnd server
Step 4, 

No worry, GitHub Copilot will go through whole project ga la

--------------------------------------------------------------
Use GitHub as code respiratory <br>
(After basic coding, I will create another GitHub respiratory to store codes)<br>
(as AWS Amplify only fetch index.html at the most top of directory)<br>
(At least under my research, I didn't found a way to change root directory of AWS Amplify))<br>

Using AWS Amplify for web hosting<br>
&nbsp;&nbsp;&nbsp;&nbsp;- Support a web link in "ugly" form. 
&nbsp;&nbsp;&nbsp;&nbsp;- Enough to use if only use for report match result<br>
&nbsp;&nbsp;&nbsp;&nbsp;- As planning providing QR code to scan on big screen instead of enter URL by players<br>
&nbsp;&nbsp;&nbsp;&nbsp;- 