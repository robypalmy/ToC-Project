<template>
  <div class="about-page">
    <h1>About Page</h1>
    <div class="card-container">
      <div class="card">
        <img src="team1.jpg" alt="Team 1" />
        <h2>Team 1</h2>
        <p>Description of Team 1</p>
      </div>
      <div class="card">
        <img src="team2.jpg" alt="Team 2" />
        <h2>Team 2</h2>
        <p>Description of Team 2</p>
      </div>
      <div class="card">
        <img src="team3.jpg" alt="Team 3" />
        <h2>Team 3</h2>
        <p>Description of Team 3</p>
      </div>
      <div class="card">
        <img src="team4.jpg" alt="Team 4" />
        <h2>Team 4</h2>
        <p>Description of Team 4</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.about-page {
  height: 100vh; /* Set the height to fill the entire viewport */
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.card-container {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
}

.card {
  width: 250px;
  padding: 20px;
  background-color: #f0f0f0;
  border-radius: 8px;
  text-align: center;
}

.card img {
  width: 100%;
  height: auto;
  border-radius: 8px;
}

.card h2 {
  margin-top: 10px;
}

.card p {
  margin-top: 5px;
}
</style>
