# Multiple Criteria Decision Making using TOPSIS
 Calculates the topsis score from all int and float columns in data and gives the ranks of rows in order of topsis score.
#### Inputs

* ```"FileName.csv"``` - name of file containing input data
* ```weights``` - weights to be assigned to each column in topsis (no. of weights
        should be equal to total no. of int and float columns)
* ```impacts``` - impact that each column should have on topsis score (+ or - , where +     means high value of that record is desirable!)

#### Outputs
A dictionary of the form ```
{
    ranks: <list of ranks>,
    topsis_scores: <list of topsis scores>
    }```
### How to run
Run thorugh cmd line as:
```sh
python topsis.py <InputDataFile> <Weights> <Impacts>
```
Example:
```sh
python topsis.py myData.csv “1,2,1,1” “+,+,-,+”
```

License
----

MIT


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
