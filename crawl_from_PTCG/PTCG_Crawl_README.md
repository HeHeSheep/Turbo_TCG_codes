# PTCG 官網卡片爬取

This branch is to work for codes of PTCG crawler.

Progress: Code built. Simple test is done. 

Future work: A test based on Whole set of cards. (e.g. sv4a / SV5)

Also, complete Code improve below to improve code maintenance and code line reusability.  
Code improve should build another branch to do it. 
Merch this branch after sv4a test is complete. 

After this future, Merge of Main branch is ready. 

Code improve:

    0. If needed to sell it, need to add a part to define download path / adjust the related path
    1. Add part to capture HTML block for card description.
    2. Using an array to store card information.
    3. Array can be used to print repeatedly with while/for loop. 
    4. Array should based on those heading that Shopify input CSV needs. 

Problem not fixed: Cannot select Rarity of cards, as no Rarity information in HTML codes. 