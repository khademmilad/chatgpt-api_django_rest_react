import React, { useState, useEffect } from 'react';
import { Row, Col, Container } from '@themesberg/react-bootstrap';
import AccordionComponent from "../../components/AccordionComponent";
import Documentation from "../../components/Documentation";

export default () => {
  const [accordionData, setAccordionData] = useState([]);

  useEffect(() => {
    fetchAccordionData();
  }, []);

  const fetchAccordionData = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/api/posts/user/1/');
      const data = await response.json();
      setAccordionData(data);
    } catch (error) {
      console.log('Error fetching accordion data:', error);
    }
  };

  return (
    <article>
      <Container className="px-0">
        <Row className="d-flex flex-wrap flex-md-nowrap align-items-center py-4">
          <Col className="d-block mb-4 mb-md-0">
            <h1 className="h2">Accordions</h1>
            <p className="mb-0">
              Use the accordion elements to segment content and show/hide when clicking on tabs.
            </p>
          </Col>
        </Row>

        <AccordionComponent defaultKey="panel-1" data={accordionData} />
      </Container>
    </article>
  );
};
