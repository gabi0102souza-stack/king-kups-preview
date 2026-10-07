'use strict';

// Progressive enhancement: direct phone/email links work without this helper.
const helper = document.querySelector('.inquiry-helper');
const form = document.querySelector('#catering-form');
if (helper && form) {
  helper.hidden = false;
  const dateField = form.elements.namedItem('date');
  const today = new Date();
  dateField.min = [today.getFullYear(), String(today.getMonth() + 1).padStart(2, '0'), String(today.getDate()).padStart(2, '0')].join('-');
  const result = document.querySelector('#inquiry-result');
  const draft = document.querySelector('#email-draft');
  form.addEventListener('input', () => { result.hidden = true; });
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    const values = new FormData(form);
    const location = String(values.get('location')).trim();
    if (!location) {
      form.elements.namedItem('location').setCustomValidity('Please enter an event city or location.');
      form.elements.namedItem('location').reportValidity();
      return;
    }
    const date = String(values.get('date'));
    const formattedDate = new Date(`${date}T12:00:00`).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
    const body = [
      'Hi King Kups,', '', 'I would like to ask about catering for an event.', '',
      `Date: ${formattedDate}`, `Location: ${location}`,
      `Estimated guests: ${values.get('guests')}`,
      `Occasion: ${values.get('occasion') || 'To be discussed'}`, '',
      'Could you share your availability, menu options and a quote?', '', 'Thank you!'
    ].join('\r\n');
    draft.href = `mailto:kingkupsofficial@gmail.com?subject=${encodeURIComponent('King Kups catering inquiry')}&body=${encodeURIComponent(body)}`;
    result.hidden = false;
  });
  form.elements.namedItem('location').addEventListener('input', (event) => { event.target.setCustomValidity(''); });
}
