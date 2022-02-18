<template>
  <div>
    <p class="pt-5 text-xl font-semibold">{{ reviews.length }} Reviews</p>
    <div
      v-for="(review, index) in reviews"
      :key="index"
      class="p-4 border-2 mb-4 rounded"
    >
      <div class="text-sm inline-flex">
        <p class="font-medium mr-1 underline">{{ review.user }}</p>
        rates this product
        <p class="ml-1 font-bold">{{ review.rating }} / 5</p>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-5 w-5"
          viewBox="0 0 20 20"
          fill="currentColor"
        >
          <path
            d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"
          />
        </svg>
      </div>
      <p class="mt-2 text-lg font-semibold">{{ review.title }}</p>
      <div class="flex">
        <!-- <p class="text-sm mr-2">{{ review.user }}</p> -->
        <p class="text-sm font-medium">
          Posted: {{ getFormattedDate(review.date_posted) }}
        </p>
      </div>
      <p class="mt-4 font-light">{{ review.text }}</p>
      <div class="mt-4 flex items-center">
        <p class="text-sm font-medium mr-2">Helpful?</p>
        <button class="bg-gray-200 p-1 mr-2 inline-flex rounded">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-5 w-5"
            viewBox="0 0 20 20"
            fill="currentColor"
          >
            <path
              d="M2 10.5a1.5 1.5 0 113 0v6a1.5 1.5 0 01-3 0v-6zM6 10.333v5.43a2 2 0 001.106 1.79l.05.025A4 4 0 008.943 18h5.416a2 2 0 001.962-1.608l1.2-6A2 2 0 0015.56 8H12V4a2 2 0 00-2-2 1 1 0 00-1 1v.667a4 4 0 01-.8 2.4L6.8 7.933a4 4 0 00-.8 2.4z"
            /></svg
          >YES
        </button>
        <button class="bg-gray-200 p-1 mr-2 inline-flex items-center rounded">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-5 w-5"
            viewBox="0 0 20 20"
            fill="currentColor"
          >
            <path
              d="M18 9.5a1.5 1.5 0 11-3 0v-6a1.5 1.5 0 013 0v6zM14 9.667v-5.43a2 2 0 00-1.105-1.79l-.05-.025A4 4 0 0011.055 2H5.64a2 2 0 00-1.962 1.608l-1.2 6A2 2 0 004.44 12H8v4a2 2 0 002 2 1 1 0 001-1v-.667a4 4 0 01.8-2.4l1.4-1.866a4 4 0 00.8-2.4z"
            />
          </svg>
          NO
        </button>
        <a class="text-sm text-gray-400 underline" href="#">Report</a>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import moment from "moment";

export default {
  name: "Reviews",
  data() {
    return {
      reviews: [],
    };
  },
  mounted() {
    this.getReviews();
  },
  methods: {
    getFormattedDate(date) {
      return moment(date).format("ddd, MMM DD");
    },
    async getReviews() {
      const productKey = this.$route.params.key;
      await axios
        .get(`/api/review/get-reviews/${productKey}`)
        .then((response) => {
          // console.log(JSON.stringify(response.data));
          this.reviews = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>