<template>
  <div>
    <h1 class="m-4 mx-2 mb-0 m-md-5 mb-md-0 display-md-5">NOW SHOWING</h1>

    <section id="largeCarousel">
      <div
        id="demo"
        class="d-none d-md-block carousel slide bg-danger"
        data-bs-ride="carousel"
      >
        <div class="carousel-inner">
          <div
            class="carousel-item"
            v-for="(items, index) in carouselItems"
            :key="index"
            :class="{ active: index === 0 }"
          >
            <div class="container">
              <div class="row">
                <div class="p-2 my-2 col-2" v-for="item in items" :key="item">
                  <div class="card">
                    <img
                      :src="item.poster"
                      :alt="item.title"
                      class="img-fluid card-img-top"
                    />
                    <router-link
                      :to="{
                        name: 'Showtime',
                        params: { id: item.id, slug: item.slug },
                      }"
                      class="m-2 btn btn-outline-danger text-truncate"
                      href="#"
                      >{{ item.title }}
                    </router-link>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <button
          class="carousel-control-prev"
          type="button"
          data-bs-target="#demo"
          data-bs-slide="prev"
          style="width: 5vw"
        >
          <span class="carousel-control-prev-icon"></span>
        </button>
        <button
          class="carousel-control-next"
          type="button"
          data-bs-target="#demo"
          data-bs-slide="next"
          style="width: 5vw"
        >
          <span class="carousel-control-next-icon"></span>
        </button>
      </div>
    </section>

    <section id="smallCarousel">
      <div
        id="demo-small"
        class="d-md-none carousel slide bg-danger"
        data-bs-ride="carousel"
      >
        <div class="carousel-inner">
          <div
            class="carousel-item"
            v-for="(items, index) in carouselItemsSmall"
            :key="index"
            :class="{ active: index === 0 }"
          >
            <div class="container">
              <div class="row justify-content-center">
                <div class="my-2 col-auto" v-for="item in items" :key="item">
                  <div class="card" style="width: 10rem">
                    <img
                      :src="item.poster"
                      :alt="item.title"
                      class="img-fluid card-img-top"
                    />
                    <router-link
                      :to="{
                        name: 'Showtime',
                        params: { id: item.id, slug: item.slug },
                      }"
                      class="m-2 btn btn-outline-danger text-truncate"
                      href="#"
                      >{{ item.title }}
                    </router-link>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <button
          class="carousel-control-prev"
          type="button"
          data-bs-target="#demo-small"
          data-bs-slide="prev"
        >
          <span class="carousel-control-prev-icon"></span>
        </button>
        <button
          class="carousel-control-next"
          type="button"
          data-bs-target="#demo-small"
          data-bs-slide="next"
        >
          <span class="carousel-control-next-icon"></span>
        </button>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";
import NowShowingItems from "@/components/NowShowingItems.vue";

export default {
  name: "NowShowing",
  components: {
    NowShowingItems,
  },
  data() {
    return {
      carouselItems: [],
      carouselItemsSmall: [],
      nowShowing: [],
    };
  },
  mounted() {
    this.getNowShowingMovies();
  },
  methods: {
    getCarouselItems(data, numItemsPerSlide) {
      var nowShowing = [];
      var carouselItems = [];
      for (let i = 0; i < data.length; i++) {
        nowShowing.push(data[i]);
        if ((i + 1) % numItemsPerSlide === 0) {
          carouselItems.push(nowShowing);
          nowShowing = [];
        }
      }
      if (nowShowing.length > 0) {
        carouselItems.push(nowShowing);
      }
      return carouselItems;
    },
    getNowShowingMovies() {
      axios
        .get("/api/movie/get-now-showing/")
        .then((response) => {
          this.carouselItems = this.getCarouselItems(response.data, 6);
          this.carouselItemsSmall = this.getCarouselItems(response.data, 2);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

