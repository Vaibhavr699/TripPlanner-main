let spotId; 
const addToTripBtn = document.querySelectorAll('.js-add-to-trip');
addToTripBtn.forEach((tripItem)=>{
    tripItem.addEventListener('click', () => {
        spotId = tripItem.dataset.spotId;
        console.log(spotId)
    })
})

const createTripBtn = document.querySelector('.js-create-trip')
const modalContent = document.querySelector('.js-modal-content');
createTripBtn.addEventListener('click', ()=>{
    modalContent.className="";
    modalContent.innerHTML=`
<form method="GET" action="/create-trip/">
  <div class="mb-3">
    <label for="exampleInputEmail1" class="form-label">What Do You Want To Call Your Trip?</label>
    <input type="text" name="name" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
    <div id="emailHelp" class="form-text">Pro tip: Naming your trip increases odd of it being successfull</div>
    <input type="hidden" name="spot_id" value="${spotId}">
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
    `;
})

const tripItem = document.querySelector('.js-trip-item');
tripItem.addEventListener('click', () => {
    const tripId = tripItem.dataset.tripId;
    location.href = `/add-spot?tripId=${tripId}&spotId=${spotId}`;
})