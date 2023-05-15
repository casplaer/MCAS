document.addEventListener("DOMContentLoaded", function(event) {
    var myElement = document.getElementById("thr");

    

    var currentDate = new Date();

    let monday = new Date(currentDate.getTime() - currentDate.getDay() * 86400000);

    monday.setDate(monday.getDate() + 1);

    let sunday = new Date(monday.getTime() + 6 * 86400000);

    let mondayFormatted = monday.toLocaleDateString();
    let sundayFormatted = sunday.toLocaleDateString();

    var formattedDate = mondayFormatted + " – " + sundayFormatted;

    
    


    myElement.innerHTML = formattedDate;
});