<template>
  <div style="background-color: #f8d7da">
    <div class="container">
      <div class="row row-cols-md-3">
        <div class="col my-2 my-md-5 text-center">
          <h4>FOLLOW US</h4>
          <div class="d-flex flex-row col-gap justify-content-center">
            <h3 v-for="item in socialIcons" :key="item">
              <a class="text-decoration-none" href="#"
                ><i style="color: black" :class="item"></i
              ></a>
            </h3>
          </div>
        </div>
        <div class="col my-2 my-md-5 text-center">
          <h4>GET THE APP</h4>
          <div class="d-flex flex-row justify-content-center">
            <img
              class="me-2 img-fluid"
              src="../assets/appstorelogo.svg"
              alt=""
              style="max-width: 10%"
            />
            <img
              class="img-fluid"
              src="../assets/playstorelogo.svg"
              alt=""
              style="max-width: 10%"
            />
          </div>
        </div>
        <div class="w-100 d-md-none"></div>
        <div class="col my-2 my-md-5 text-center align-self-center">
          <h4>CONNECT</h4>
          <form class="d-flex justify-content-center">
            <input
              class="form-control me-2"
              type="search"
              placeholder="Enter your email"
              aria-label="Search"
            />
            <button class="btn btn-danger" type="submit">SUBMIT</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Social",
  data() {
    return {
      socialIcons: [
        "me-2 bi bi-facebook",
        "me-2 bi bi-instagram",
        "me-2 bi bi-twitter",
        "me-2 bi bi-youtube",
      ],
    };
  },
};
</script>