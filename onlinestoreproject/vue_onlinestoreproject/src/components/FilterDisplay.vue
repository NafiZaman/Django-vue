<template>
  <div>
    <div class="pt-5 px-5 md:hidden">
      <button class="pt-1 flex" type="button" data-modal-toggle="defaultModal">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-4 w-4 mr-2"
          viewBox="0 0 20 20"
          fill="currentColor"
        >
          <path
            d="M5 4a1 1 0 00-2 0v7.268a2 2 0 000 3.464V16a1 1 0 102 0v-1.268a2 2 0 000-3.464V4zM11 4a1 1 0 10-2 0v1.268a2 2 0 000 3.464V16a1 1 0 102 0V8.732a2 2 0 000-3.464V4zM16 3a1 1 0 011 1v7.268a2 2 0 010 3.464V16a1 1 0 11-2 0v-1.268a2 2 0 010-3.464V4a1 1 0 011-1z"
          />
        </svg>
        <p class="text-sm font-extrabold text-center hover:text-red-700">
          Filter
        </p>
      </button>
      <div class="py-2">
        <hr />
      </div>
    </div>

    <div class="hidden md:block">
      <FilterOptions :filters="filters" :filterName="''" />
    </div>

    <!-- Main modal -->
    <div
      id="defaultModal"
      aria-hidden="true"
      class="
        hidden
        overflow-y-auto overflow-x-hidden
        fixed
        right-0
        left-0
        top-4
        z-50
        justify-center
        items-center
        h-modal
        md:h-full md:inset-0
      "
    >
      <div class="relative px-4 w-full max-w-2xl h-full md:h-auto">
        <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
          <div
            class="
              flex
              justify-between
              items-start
              p-1
              rounded-t
              border-b
              dark:border-gray-600
            "
          >
            <button
              type="button"
              class="
                text-gray-400
                bg-transparent
                hover:bg-gray-200 hover:text-gray-900
                rounded-lg
                text-sm
                p-1.5
                ml-auto
                inline-flex
                items-center
                dark:hover:bg-gray-600 dark:hover:text-white
              "
              data-modal-toggle="defaultModal"
            >
              <svg
                class="w-5 h-5"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  fill-rule="evenodd"
                  d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                  clip-rule="evenodd"
                ></path>
              </svg>
            </button>
          </div>
          <div class="p-2 space-y-6" id="modal-body">
            <FilterOptions :filters="filters" :filterName="filterName" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import FilterOptions from "./FilterOptions.vue";

export default {
  name: "FilterDisplay",
  components: {
    FilterOptions,
  },
  data() {
    return {
      filters: {},
      filterName: "modal",
    };
  },
  mounted() {
    this.getFilters();
  },
  methods: {
    getFilters() {
      axios
        .get("/api/product/get-filters")
        .then((response) => {
          for (const key in response.data) {
            if (Object.hasOwnProperty.call(response.data, key)) {
              this.filters[key] = response.data[key];
            }
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>
    