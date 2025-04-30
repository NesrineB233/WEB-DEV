let persons = [
    { nom: "Dupont", prenom: "Jean", points: 12 },
    { nom: "Martin", prenom: "Sophie", points: 15 },
    { nom: "Bernard", prenom: "Luc", points: 8 }
  ];
  
  let lignes = 0;
  let total_points = 0;
  
  function doInsertRowTable(num, nom, prenom, points) {
    const table = document.getElementById("person_table").getElementsByTagName('tbody')[0];
    const newRow = table.insertRow();
  
    newRow.insertCell(0).textContent = num;
    newRow.insertCell(1).textContent = nom;
    newRow.insertCell(2).textContent = prenom;
    newRow.insertCell(3).textContent = points;
  
    const checkboxCell = newRow.insertCell(4);
    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkboxCell.appendChild(checkbox);
  }
  
  function doInsert(nom, prenom, points) {
    lignes++;
    total_points += points;
    doInsertRowTable(lignes, nom, prenom, points);
    update_summary();
  }
  
  function update_summary() {
    document.getElementById("nb_lignes").textContent = `${lignes} ligne(s)`;
    document.getElementById("total_points").textContent = `Total point(s) = ${total_points}`;
  }
  
  function init() {
    for (let p of persons) {
      doInsert(p.nom, p.prenom, p.points);
    }
  }
  
  function consoleTableau() {
    console.log(persons);
  }
  
  window.onload = init;
  