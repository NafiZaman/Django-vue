<template>
  <div>
    <div class="d-none d-md-block bg-dark text-light">
      <div class="mx-5 row">
        <div class="col text-center">
          <span>
            <a class="text-decoration-none link-light" href="#"
              ><small>Login</small></a
            >
            |
            <a class="text-decoration-none link-light" href="#"
              ><small>Signup</small></a
            >
          </span>
        </div>
        <div class="col text-center">
          <h6 class="m-0 p-0">
            <small
              ><i class="bi bi-shield-fill-plus" style="color: red"></i>
              <a class="text-decoration-none text-light" href="#">
                OUR COVID-19 RESTRICTIONS</a
              ></small
            >
          </h6>
        </div>
        <div class="col text-center">
          <img
            src="https://images.fandango.com/cms/assets/6a3582d0-cf05-11eb-a507-3be98bb99253--studios-banner-dark.png"
            alt="studios-banner"
            class="img-fluid"
          />
        </div>
      </div>
    </div>
    <div class="d-md-none container">
      <div class="row row-cols-1">
        <!-- <div class="col bg-danger text-dark">
          <div class="d-flex">
            <div>
              <p class="m-0">
                <small
                  ><strong
                    ><i class="me-1 bi bi-shield-fill-plus"></i>OUR COVID-19
                    RESTRICTIONS</strong
                  ></small
                >
              </p>
            </div>
            <div class="ms-auto">
              <button class="p-0 text-decoration-none text-light btn btn-link">
                <small><strong>READ MORE</strong></small>
              </button>
            </div>
          </div>
        </div> -->
        <div class="col bg-dark text-light">
          <img
            src="https://images.fandango.com/cms/assets/6a3582d0-cf05-11eb-a507-3be98bb99253--studios-banner-dark.png"
            alt="studios-banner"
            class="img-fluid"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "InfoBar",
};
</script>

