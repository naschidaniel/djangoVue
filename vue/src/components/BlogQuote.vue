<template>
  <div class="mt-10 w-full shadow-md rounded border border-black-200">
    <div class="m-5 md:flex">
      <img
        class="rounded-full w-40 h-40 md:w-48 md:h-48 mx-auto md:my-auto"
        :src="getBlogQuoteById(blogQuoteID).mainImage_url"
      />
      <div
        class="text-center my-auto mt-3 md:m-10 bg-gray-200 rounded-lg p-3 font-blogCard"
      >
        <span class="text-2xl text-red-600 text-content">
          {{ getBlogQuoteById(blogQuoteID).title }}
        </span>
        <p class="text-lg text-gray-700">
          {{ getBlogQuoteById(blogQuoteID).content }}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "blogCategory",
  props: {
    blogQuoteID: Number,
  },
  computed: mapGetters(["getBlogQuoteById"]),
};
</script>
