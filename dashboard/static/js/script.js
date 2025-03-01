document.addEventListener("DOMContentLoaded", function () {
    fetch("/api/data/")
        .then(response => response.json())
        .then(data => {
            let tableBody = document.getElementById("data-body");
            tableBody.innerHTML = "";

            let labels = [];
            let intensityData = [];

            data.forEach(item => {
                let row = `<tr>
                    <td>${item.title}</td>
                    <td>${item.country}</td>
                    <td>${item.intensity}</td>
                    <td>${item.likelihood}</td>
                    <td>${item.relevance}</td>
                </tr>`;
                tableBody.innerHTML += row;

                // Collect data for chart
                labels.push(item.country || "Unknown");
                intensityData.push(item.intensity);
            });

            // Initialize DataTable
            new simpleDatatables.DataTable("#data-table");
             function getRandomColor() {
                return `rgba(${Math.floor(Math.random() * 255)}, ${Math.floor(Math.random() * 255)}, ${Math.floor(Math.random() * 255)}, 0.6)`;
            }
            let backgroundColors = labels.map(() => getRandomColor());

            // Render Chart
            const ctx = document.getElementById("myChart").getContext("2d");
            new Chart(ctx, {
                type: "bar",
                data: {
                    labels: labels,
                    datasets: [{
                        label: "Intensity by Country",
                        data: intensityData,
                        backgroundColor: "rgba(75, 192, 192, 0.2)",
                        borderColor: "rgba(75, 192, 192, 1)",
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
            
        })
        .catch(error => console.error("Error fetching data:", error));
});



