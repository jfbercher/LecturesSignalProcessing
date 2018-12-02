#perl -pi -e s#\[Index\]\(([\S]*)\)#\<a href="\1"\>Index\<\/a\>#g Grad_algo.html
htmlFile="Grad_algo.html"
perl -pi -e s#"\[Index\]\(([\S]*)\)"#"\<a href=\"\\1\"\>Index\<\/a\>"#g Grad_algo.html
perl -pi -e s#"\[Back\]\(([\S]*)\)"#"\<a href=\"\\1\"\>Back\<\/a\>"#g $htmlFile
perl -pi -e s#"\[Next\]\(([\S]*)\)"#"\<a href=\"\\1\"\>Next\<\/a\>"#g $htmlFile
