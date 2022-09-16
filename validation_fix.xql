xquery version "3.1";

let $data := collection("/jingbao/")//fold
let $pseudo-paragraph := $data//div[lb]

for $fix in $pseudo-paragraph
let $ins := element div { $fix/@*, <p>{ $fix/node() }</p>}

return
    if (data($fix/@type)) then ( update replace $fix with $ins )
    else ( update rename $fix as 'p' )