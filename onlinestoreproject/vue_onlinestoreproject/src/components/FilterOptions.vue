<template>
  <div>
    <div v-for="(filterItems, filterType) in filters" :key="filterType">
      <p class="pb-2 font-bold capitalize">{{ filterType }}</p>
      <div :class="getClass(filterItems.length)">
        <div class="py-1" v-for="(item, index) in filterItems" :key="index">
          <input
            :type="getInputType(filterType)"
            :name="filterType + filterName"
            class="filter-button"
            :class="item.key"
            @change="applyFilter($event, filterType, item.key)"
          />
          <label
            v-if="
              filterType == 'category' ||
              filterType == 'availability' ||
              filterType == 'brands'
            "
            :for="item.key"
            class="font-light capitalize"
            >{{ item.name }}</label
          >
          <label v-else :for="item.key" class="font-light capitalize">
            &#2547;{{ item.min }} - &#2547;{{ item.max }}
          </label>
        </div>
      </div>
      <div class="py-2">
        <hr />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "FilterOptions",
  // props: ["filterItems", "filterType"],
  props: ["filters", "filterName"],
  // mounted() {
  //   console.log(JSON.stringify(this.filters));
  // },
  data() {
    return {
      message: "",
    };
  },
  methods: {
    getInputType(filterType) {
      if (filterType == "category" || filterType == "availability")
        return "checkbox";
      else return "radio";
    },
    getClass(numItems) {
      if (numItems <= 3) {
        return "overflow-y-auto";
      } else {
        return "overflow-y-auto h-40";
      }
    },
    applyFilter(event, filterType, itemKey) {
      const obj = {};
      obj[filterType] = itemKey;

      const checkedState = event.target.checked;
      // console.log(checkedState);

      this.$store.commit("SET_FILTERS", obj);
      var inputs = document.getElementsByClassName(itemKey);

      // for (const [key, value] of Object.entries(this.$store.state.filters)) {
      //   var inputs = document.querySelectorAll(`input[name=${key}]`);

      // console.log(inputs.length);
      for (let i = 0; i < inputs.length; i++) {
        if (inputs[i] !== event.target) {
          // console.log("found something");
          inputs[i].checked = checkedState;
        }
      }
    },
  },
};
</script>