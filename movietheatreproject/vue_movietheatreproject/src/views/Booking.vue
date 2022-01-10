<template>
  <div class="container" style="max-width: 100vw">
    <div class="row bg-dark text-light">
      <div class="p-3 col">
        <div class="d-flex flex-row justify-content-md-center">
          <div class="me-2">
            <img
              class="img-fluid border border-light"
              :src="bookingData.poster"
              :alt="bookingData.title"
            />
          </div>
          <div class="d-flex flex-column">
            <div>
              <p class="mb-5 h3">{{ bookingData.title }}</p>
            </div>
            <div class="mt-auto">
              <p class="mb-0 h5">
                {{ bookingData.date }}, at {{ bookingData.time }}, Hall 3
              </p>
              <p class="mb-0">{{ bookingData.theatre }}</p>
              <p class="mb-0 muted">
                <small>{{ bookingData.location }}</small>
              </p>
              <a class="text-decoration-none text-danger" href="#"
                ><i class="bi bi-shield-fill-plus" style="color: red"></i>
                <strong>Theatre's COVID-19 restrictions</strong></a
              >
            </div>
          </div>
        </div>
      </div>
    </div>
    <Ticket />
  </div>
</template>

<script>
import Ticket from "@/components/Ticket.vue";

export default {
  name: "Booking.vue",
  components: {
    Ticket,
  },
  props: ["title", "poster", "date", "time", "theatre", "location"],
  data() {
    return {
      bookingData: {},
    };
  },
  mounted() {
    this.getBookingInfo();
  },
  methods: {
    getBookingInfo() {
      if (localStorage.getItem("bookingData")) {
        this.bookingData = JSON.parse(localStorage.getItem("bookingData"));
      } else {
        this.bookingData = {
          title: this.title,
          poster: this.poster,
          time: this.time,
          theatre: this.theatre,
          location: this.location,
          date: this.date,
        };
        this.$store.commit("setBookingData", this.bookingData);
      }
    },
  },
};
</script>