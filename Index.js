document.querySelector("#searchBtn").addEventListener("click", 
  
    function dataFetch(e) {
        console.log(e)
        e.preventDefault();
      console.log("fetchdata");
     
       const keyword = document.getElementById("seachText").value;
      if (keyword.length != 0) {
         fetch(`http://127.0.0.1:5000/twitter/${keyword}`)
          .then(function (response) {
            console.log("json", keyword);
            return response.json();
          })
          .then(function (apiJsonData) {
            document.getElementById("seachText").value = "";
           document.getElementById("search-query").innerText = keyword;
            const myTableBody = document.getElementById("html-data-table-body");
            if (myTableBody.hasChildNodes()) {
              myTableBody.innerHTML = "";
             renderDataInTheTable(apiJsonData);
            } else {
              renderDataInTheTable(apiJsonData);
           }
          });
      }
      function renderDataInTheTable(searchData) {
        // console.log(searchData);
        const mytable = document.getElementById("html-data-table-body");
    
        searchData.tweets.forEach((data) => {
          let newRow = document.createElement("tr");
          console.log(Object.keys(data));
          Object.values(data).forEach((value) => {
            let cell = document.createElement("td");
            cell.innerText = value;
            newRow.appendChild(cell);
          });
          mytable.appendChild(newRow);
        });
      }
    });
