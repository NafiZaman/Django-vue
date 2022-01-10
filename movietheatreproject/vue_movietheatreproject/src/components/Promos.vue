<template>
  <div>
    <div class="card m-5 mb-0 shadow-sm">
      <div class="card-body">
        <section>
          <h3 class="d-none d-md-block">COMING SOON</h3>
          <div class="d-none d-md-block mb-5 container">
            <div class="row row-cols-6">
              <div
                class="col-2"
                v-for="(movie, index) in comingSoon"
                :key="index"
              >
                <div class="card border-0">
                  <img
                    class="img-fluid card-img-top"
                    :src="movie.poster"
                    :alt="movie.title"
                  />
                  <div class="p-0 card-body text-center">
                    <p class="m-0 h6">{{ movie.title }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <section>
          <h3>MOVIE NEWS</h3>
          <section v-for="(item, index) in news" :key="index">
            <div class="p-0 m-0 mb-5 container">
              <div class="row align-items-center justify-content-between">
                <div class="col-md">
                  <img class="img-fluid" :src="item.cover_image" alt="" />
                </div>
                <div class="mb-auto col-md">
                  <h4>{{ item.title }}</h4>
                  <p class="d-none d-md-block lead">{{ item.text }}.........</p>
                  <a href="#" class="btn btn-danger">
                    <i class="bi bi-chevron-right"></i> Read More
                  </a>
                </div>
              </div>
            </div>
          </section>
        </section>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Promos",
  data() {
    return {
      comingSoon: [],
      news: [],
    };
  },
  mounted() {
    this.getComingSoon();
    this.getNews();
  },
  methods: {
    getComingSoon() {
      axios
        .get("/api/movie/get-coming-soon/")
        .then((response) => {
          for (let i = 0; i < response.data.length; i++) {
            this.comingSoon.push(response.data[i]);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    getNews() {
      axios
        .get("/api/news/get-news/")
        .then((response) => {
          for (let i = 0; i < response.data.length; i++) {
            this.news.push(response.data[i]);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>