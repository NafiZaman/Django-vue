<template>
  <div>
    <div
      class="carousel-item"
      v-for="(movies, index) in carouselItems"
      :key="index"
      :class="{ active: index === 0 }"
    >
      <div class="container">
        <div class="row">
          <div class="p-2 my-2 col-2" v-for="movie in movies" :key="movie">
            <div class="card">
              <img
                :src="movie.poster"
                :alt="movie.title"
                class="img-fluid card-img-top"
              />
              <router-link
                :to="{
                  name: 'Showtime',
                  params: { id: movie.id, slug: movie.slug },
                }"
                class="m-2 btn btn-outline-danger text-truncate"
                href="#"
                >{{ movie.title }}
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "NowShowingItems",
  props: ["carouselItems"],
  mounted() {
    console.log(this.movies);
  },
};
</script>