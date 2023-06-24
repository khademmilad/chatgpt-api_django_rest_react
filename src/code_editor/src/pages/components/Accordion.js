import React, { useState } from 'react';
import { Accordion, Card, Button } from 'react-bootstrap';

const AccordionComponent = ({ defaultKey, data }) => {
  const [activeKey, setActiveKey] = useState(defaultKey);

  const toggleAccordion = (eventKey) => {
    setActiveKey(eventKey === activeKey ? null : eventKey);
  };

  return (
    <Accordion activeKey={activeKey}>
      {data.map((item) => (
        <Card key={item.id}>
          <Card.Header>
            <Accordion.Toggle
              as={Button}
              variant="link"
              eventKey={item.eventKey}
              onClick={() => toggleAccordion(item.eventKey)}
            >
              {item.title}
            </Accordion.Toggle>
          </Card.Header>
          <Accordion.Collapse eventKey={item.eventKey}>
            <Card.Body>{item.description}</Card.Body>
          </Accordion.Collapse>
        </Card>
      ))}
    </Accordion>
  );
};

export default AccordionComponent;
