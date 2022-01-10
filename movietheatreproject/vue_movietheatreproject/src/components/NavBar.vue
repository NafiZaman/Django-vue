<template>
  <nav
    class="
      p-0
      navbar navbar-light
      bg-light
      sticky-top
      border-bottom border-2 border-danger
    "
  >
    <div class="m-0 p-0 container-fluid justify-content-start">
      <a class="m-0 navbar-brand" href="/">
        <img
          src="../assets/ticket-2.svg"
          alt="site-logo"
          width="100"
          height="40"
        />
      </a>
      <div class="col d-flex">
        <div class="d-none d-md-block">
          <form class="d-flex">
            <input
              class="form-control me-2"
              type="search"
              placeholder="Enter Location or Movie"
              aria-label="Search"
            />
            <button class="btn btn-danger" type="submit">
              <i class="bi bi-search"></i>
            </button>
          </form>
        </div>
        <div class="d-none d-md-block px-5 ms-auto my-auto">
          <a href="#" class="link-dark me-2"><strong>SHOWTIME</strong> </a>
          <a href="#" class="link-dark me-2"><strong>THEATRES</strong> </a>
          <a href="#" class="link-dark me-2"><strong>MOVIES</strong> </a>
          <a href="#" class="link-dark"><strong>NEWS</strong> </a>
        </div>
        <div class="d-md-none ms-auto">
          <form class="mx-2 d-flex">
            <input
              class="form-control-sm me-2"
              type="search"
              placeholder="Enter Location or Movie"
              aria-label="Search"
            />
            <button class="btn btn-sm btn-danger" type="submit">
              <i class="bi bi-search"></i>
            </button>
          </form>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavBar",
};
</script>

