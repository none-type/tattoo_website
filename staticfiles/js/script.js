        // Get all gallery images
		const galleryItems = document.querySelectorAll('.grid-item img');

		// Add click event listeners to all gallery images
		galleryItems.forEach(item => {
		    item.addEventListener('click', function() {
		        openModal(this.src); // Pass the clicked image's src to openModal
		    });
		});

		// Disable scroll without hiding the scrollbar
		function disableScroll() {
		    window.addEventListener('scroll', preventScroll, { passive: false });
		    window.addEventListener('wheel', preventScroll, { passive: false });
		    window.addEventListener('touchmove', preventScroll, { passive: false });
		}

		function preventScroll(e) {
		    e.preventDefault();
		    e.stopPropagation();
		    return false;
		}

		// Enable scroll when modal is closed
		function enableScroll() {
		    window.removeEventListener('scroll', preventScroll);
		    window.removeEventListener('wheel', preventScroll);
		    window.removeEventListener('touchmove', preventScroll);
		}

		function openModal(imageSrc) {
		    const modal = document.getElementById('modal');
		    const modalImage = document.getElementById('modal-image');
		    modalImage.src = imageSrc;
		    modal.classList.add('active'); // Show the modal
		    disableScroll(); // Lock scrolling
		}

		function closeModal() {
		    const modal = document.getElementById('modal');
		    modal.classList.remove('active'); // Hide the modal
		    enableScroll(); // Unlock scrolling
		}



		function toggleMenu() {
            const navbarLinks = document.querySelector('.navbar-links');
            navbarLinks.classList.toggle('active');
        }