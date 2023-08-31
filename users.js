

// Create a user with password
// use admin;

// Additionally if you use Studio 3T you could manager users with its built-in User and Role management


db.createUser({
  user: "myuser",
  pwd: "mypassword",
  roles: [
    { role: "read", db: "mydatabase" }
  ]
});
