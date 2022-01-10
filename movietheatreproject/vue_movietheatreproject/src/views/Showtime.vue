<template>
  <div>
    <div class="card m-2 m-md-5 mb-0 shadow-sm">
      <div class="p-0 p-md-3 card-body">
        <div class="container">
          <section>
            <div class="p-3 mb-5 row border rounded border-danger">
              <div class="col col-md-2 text-center mb-2 mb-md-0">
                <img :src="poster" :alt="title" class="img-fluid rounded" />
                <p class="m-0 p-0 text-center lead">{{ title }}</p>
              </div>
              <div class="col-6 d-none d-md-block">
                <p style="text-align: justify">
                  <strong>Synopsis: </strong>{{ synopsis }}
                  <a href="#" class="me-1 link-danger text-decoration-none"
                    ><i class="bi bi-box-arrow-up-right"></i>
                  </a>
                </p>
              </div>
              <div class="w-100 d-md-none"></div>
              <div class="col">
                <p class="m-0" v-for="(value, name) in details" :key="name">
                  <strong>{{ name }}: </strong>{{ value }}
                </p>
              </div>
            </div>
          </section>

          <section>
            <div class="d-flex flex-row">
              <p class="h6 ms-0 me-2 p-0">
                <strong>THEATRES NEAR </strong>
              </p>
              <p class="h6 ms-0 p-0 text-danger">
                <strong
                  ><i class="bi bi-geo-alt-fill"></i> DHAKA, BANGLADESH</strong
                >
              </p>
            </div>
          </section>

          <!-- <section class="d-md-none">
            <h1>as</h1>
          </section> -->

          <section>
            <div
              class="mb-2 row row-cols-1"
              v-for="theatre in theatreInfo"
              :key="theatre"
            >
              <div class="col card border border-2 rounded">
                <div class="card-body">
                  <div class="d-none d-md-block">
                    <p class="h4">
                      <i class="me-2 bi bi-heart"></i>
                      <strong>{{ theatre.name }}</strong>
                    </p>
                    <p class="mb-5 text-danger h6">
                      <strong>{{ theatre.location }}</strong>
                    </p>
                  </div>
                  <div class="d-md-none">
                    <p class="h6">
                      <i class="me-2 bi bi-heart"></i>
                      <strong>{{ theatre.name }}</strong>
                    </p>
                    <p class="mb-5 text-danger h6">
                      <strong
                        ><small>{{ theatre.location }}</small></strong
                      >
                    </p>
                  </div>
                  <hr />
                  <div class="d-flex flex-wrap">
                    <router-link
                      :to="{
                        name: 'Booking',
                        params: {
                          title: title,
                          poster: poster,
                          date: 'Tue, 21st Feb',
                          time: showtime,
                          theatre: theatre.name,
                          location: theatre.location,
                        },
                      }"
                      class="d-md-none m-2 btn btn-danger btn-sm"
                      v-for="showtime in theatre.showtimes"
                      :key="showtime"
                    >
                      {{ showtime }}
                    </router-link>
                    <router-link
                      :to="{
                        name: 'Booking',
                        params: {
                          title: title,
                          poster: poster,
                          date: 'Tue, 21st Feb',
                          time: showtime,
                          theatre: theatre.name,
                          location: theatre.location,
                        },
                      }"
                      class="d-none d-md-block me-2 btn btn-danger"
                      v-for="showtime in theatre.showtimes"
                      :key="showtime"
                    >
                      {{ showtime }}
                    </router-link>
                  </div>
                </div>
              </div>
            </div>
          </section>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Showtime",
  // props: ["movieID"],
  data() {
    return {
      title: "",
      poster: "",
      synopsis: "",
      details: "",
      theatreInfo: [],
    };
  },
  mounted() {
    this.getMovieInfo();
  },
  methods: {
    getMovieInfo() {
      const movieID = this.$route.params.id;
      axios
        .get(`api/showtime/get-showtime/${movieID}/`)
        .then((response) => {
          this.title = response.data["movie"]["title"];
          this.poster = response.data["movie"]["poster"];
          this.synopsis = response.data["movie"]["synopsis"];
          this.details = response.data["movie"]["details"];

          for (let i = 0; i < response.data["theatre_info"].length; i++) {
            this.theatreInfo.push(response.data["theatre_info"][i]);
            const showtimes = response.data["theatre_info"][i]["showtimes"];
            for (let j = 0; j < showtimes.length; j++) {
              const element = showtimes[j].split(":");
              if (parseInt(element[0]) < 12) {
                showtimes[j] = element[0] + ":" + element[1] + " AM";
              } else {
                showtimes[j] =
                  (parseInt(element[0]) - 12).toString() +
                  ":" +
                  element[1] +
                  " PM";
              }
            }
          }
        })
        .catch((error) => {
          console.log(JSON.stringify(error));
        });
    },
  },
};
</script>