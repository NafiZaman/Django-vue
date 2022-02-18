<template>
  <div>
    <p class="pt-5 text-xl font-semibold">Specifications</p>
    <div class="flex flex-col">
      <div class="flex">
        <p class="py-1 mr-1 font-medium">Brand:</p>
        <p class="py-1 capitalize">{{ brand }}</p>
      </div>
      <div class="py-1">
        <hr />
      </div>
      <div class="mt-1 flex">
        <p class="py-1 mr-1 font-medium">Weight:</p>
        <p class="py-1 capitalize">{{ weight }} KG</p>
      </div>
      <div class="py-1">
        <hr />
      </div>
      <div class="mt-1 flex">
        <p class="py-1 mr-1 font-medium">Dimensions:</p>
        <p class="py-1 capitalize">{{ dimensions }} KG</p>
      </div>
      <div class="py-1">
        <hr />
      </div>
      <div class="mt-1 flex">
        <p class="py-1 mr-1 font-medium">Categories:</p>
        <div class="py-1 truncate">
          <p v-for="c in category" :key="c" class="capitalize inline-block">
            {{ c }},
          </p>
        </div>
      </div>
      <div class="py-1">
        <hr />
      </div>
      <div class="mt-1 flex">
        <p class="py-1 mr-1 font-medium">Average rating:</p>
        <p class="py-1 capitalize">{{ avg_rating }}/5</p>
      </div>
      <div class="py-1">
        <hr />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Specifications",
  props: ["weight", "dimensions", "category", "brand", "avg_rating"],
};
</script>
